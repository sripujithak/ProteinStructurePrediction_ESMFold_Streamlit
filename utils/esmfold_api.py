import requests
import biotite.structure.io as bsio

ESMFOLD_API_URL = "https://api.esmatlas.com/foldSequence/v1/pdb/"

class ESMFoldError(Exception):
    """Custom exception for ESMFold API errors."""
    pass


def predict_structure(sequence: str, timeout: int = 120):
    """
    Send a protein sequence to the ESMFold API and return:
    - pdb_string: predicted structure in PDB format
    - plddt: average confidence score
    """
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    try:
        response = requests.post(
            ESMFOLD_API_URL,
            headers=headers,
            data=sequence,
            timeout=timeout,
        )
        response.raise_for_status()

    except requests.exceptions.Timeout:
        raise ESMFoldError(
            "The ESMFold server timed out. "
            "Try again later or use a shorter sequence."
        )

    except requests.exceptions.HTTPError as e:
        if response.status_code == 504:
            raise ESMFoldError(
                "ESMFold is currently overloaded (504 Gateway Timeout). "
                "Please try again later."
            )
        else:
            raise ESMFoldError(f"ESMFold API error: {e}")

    except requests.exceptions.RequestException as e:
        raise ESMFoldError(f"Network error: {e}")

    pdb_string = response.content.decode("utf-8")

    with open("predicted.pdb", "w") as f:
        f.write(pdb_string)

    structure = bsio.load_structure("predicted.pdb", extra_fields=["b_factor"])
    plddt = round(structure.b_factor.mean(), 5)

    return pdb_string, plddt
