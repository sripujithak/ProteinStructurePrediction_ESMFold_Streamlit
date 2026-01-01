# ESMFold Protein Structure Predictor

The **ESMFold Streamlit App** is an interactive web application for predicting and visualizing **3D protein structures** from amino acid sequences. It leverages the **ESMFold (ESM-2) model** via the **ESM Atlas API**, enabling high-accuracy structure prediction **without heavy local compute requirements**.

---

## Features

- **Flexible input**
  - Upload FASTA files (`.fasta`, `.fa`)
  - Manually paste amino acid sequences

- **Interactive 3D visualization**
  - Powered by **stmol** and **py3Dmol**
  - Switch between **Cartoon (ribbon)** and **Stick** representations
  - Optional **spin toggle** for continuous rotation

- **Export support**
  - Download predicted structures as `.pdb` files
  - Compatible with tools like **PyMOL** and **ChimeraX**

- **Modern UI**
  - Clean, responsive interface built with **Streamlit**

---

## Installation

Clone the repository:

    git clone https://github.com/yourusername/esmfold-streamlit.git
    cd esmfold-streamlit

Install dependencies:

    pip install -r requirements.txt

---

## Usage

Run the Streamlit app locally:

    streamlit run app.py

Open the provided local URL in your browser to start predicting protein structures.

---

## Sidebar & Settings

### Input Options
- **Upload FASTA file**
  - Supports `.fasta` and `.fa` formats
- **Manual input**
  - Paste raw amino acid sequences directly

### Visualization Options
- **Cartoon**
  - Best for visualizing secondary structures (alpha-helices, beta-sheets)
- **Stick**
  - Best for atomic-level details and side chains
- **Spin structure**
  - Keeps the protein model rotating continuously

### Prediction
- **Predict button**
  - Sends the sequence to the ESMFold API and renders the result

---

## Project Structure

    esmfold-streamlit/
    ├── app.py
    ├── requirements.txt
    ├── utils/
    │   ├── __init__.py
    │   ├── fasta.py
    │   ├── esmfold_api.py
    │   └── visualization.py
    └── README.md

---

## Important Notes

- **Sequence length limits**
  - The ESMFold API typically supports sequences up to ~400 residues
  - Longer sequences may cause timeouts or errors

- **Internet required**
  - An active internet connection is necessary to access the ESM Atlas API

---

## Contributing

Contributions are welcome and appreciated.
Feel free to open an issue or submit a pull request.
