import streamlit as st

from utils import (
    render_mol,
    predict_structure,
    ESMFoldError,
    parse_fasta,
)


st.set_page_config(
    page_title="ESMFold Protein StructurePredictor",
    layout="wide",
)

st.sidebar.title(" ESMFold Protein Structure Predictor")
st.sidebar.write('[*ESMFold*](https://esmatlas.com/about) is an end-to-end single sequence protein structure predictor based on the ESM-2 ' \
'language model. For more information, read the [research article](https://www.biorxiv.org/content/10.1101/2022.07.20.500902v2) and the [news' \
' article](https://www.nature.com/articles/d41586-022-03539-1) published in *Nature*.')



st.sidebar.subheader(" Upload FASTA file (optional)")
uploaded_file = st.sidebar.file_uploader(
    "Upload a FASTA file",
    type=["fasta", "fa", "faa"],
)

st.sidebar.subheader("Visualization Style")
viz_style = st.sidebar.selectbox(
    "Choose structure representation",
    options=["Cartoon", "Stick"],
)
st.sidebar.subheader("Visualization Options")


spin_structure = st.sidebar.checkbox(
    "Spin structure",
    value=True,
)



DEFAULT_SEQ = (
    "MGSSHHHHHHSSGLVPRGSHMRGPNPTAASLEASAGPFTVRSFTVSRPSGYGAGTVYYPTNAGGTVGAIAIVPGYTARQ"
    "SSIKWWGPRLASHGFVVITIDTNSTLDQPSSRSSQQMAALRQVASLNGTSSSPIYGKVDTARMGVMGWSMGGGGSLISA"
    "ANNPSLKAAAPQAPWDSSTNFSSVTVPTLIFACENDSIAPVNSSALPIYDSMSRNAKQFLEINGGSHSCANSGNSNQAL"
    "IGKKGVAWMKRFMDNDTRYSTFACENPNSTRVSDFRTANCSLEDPAANKARKEAELAAATAEQ"
)

sequence = None

if uploaded_file is not None:
    try:
        fasta_text = uploaded_file.read().decode("utf-8")
        sequence = parse_fasta(fasta_text)
        st.sidebar.success("FASTA file loaded successfully.")
    except Exception as e:
        st.sidebar.error(f"FASTA parsing error: {e}")
else:
    sequence = st.sidebar.text_area(
        "Or paste protein sequence manually",
        DEFAULT_SEQ,
        height=275,
    )

MAX_LEN = 400

if st.sidebar.button("Predict"):
    if not sequence or not sequence.strip():
        st.error("Please provide a protein sequence or upload a FASTA file.")

    elif len(sequence) > MAX_LEN:
        st.warning(
            f"Sequence length is {len(sequence)} amino acids. "
            "Long sequences may cause the ESMFold API to timeout."
        )

    else:
        try:
            with st.spinner("Predicting protein structure..."):
                pdb_string, plddt = predict_structure(sequence)

            st.subheader("Visualisation of the Predicted Protein Structure")
            render_mol(
                pdb_string,
                style=viz_style.lower(),
                spin=spin_structure,  # still optional
            )



            st.subheader(" Prediction Confidence (plDDT)")
            st.write(
                "plDDT is a per-residue confidence score (0–100). "
                "Higher values indicate more reliable predictions."
            )
            st.info(f"Average plDDT: {plddt}")

            st.download_button(
                label="⬇️ Download PDB",
                data=pdb_string,
                file_name="predicted.pdb",
                mime="text/plain",
            )

        except ESMFoldError as e:
            st.error(str(e))
