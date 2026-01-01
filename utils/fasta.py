def parse_fasta(fasta_text: str) -> str:
    """
    Parse a FASTA file and return the sequence as a single string.
    """
    lines = fasta_text.strip().splitlines()

    if not lines or not lines[0].startswith(">"):
        raise ValueError("Invalid FASTA format: missing header line ('>').")

    sequence_lines = [
        line.strip()
        for line in lines
        if not line.startswith(">")
    ]

    sequence = "".join(sequence_lines).upper()

    if not sequence.isalpha():
        raise ValueError("FASTA sequence contains invalid characters.")

    return sequence
