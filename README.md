# ESMFold Protein Structure Predictor Using Streamlit

ESMFold Streamlit App is an interactive web application to predict and visualize protein 3D structures from amino acid sequences using the ESMFold model (ESM-2) via the ESM Atlas API. Learn more at https://esmatlas.com

It allows users to upload FASTA files or enter sequences manually, and provides an interactive 3D visualization of the predicted protein structure.



---

##  Features

Predict protein structures from:  

- **FASTA file upload**  
- **Manual sequence input**  

**Visualization Options:**  

- 3D visualization with Cartoon or Stick representation  
- Spin toggle for dynamic rotation  
- Download PDB file of the predicted structure  

**App Highlights:**  

- Simple, responsive interface built with Streamlit  
- Run locally or deploy on Streamlit Cloud  

---

##  Installation

**Clone the repository:**

```bash
git clone https://github.com/yourusername/esmfold-streamlit.git
cd esmfold-streamlit

Install dependencies:

```bash
Copy code
pip install -r requirements.txt


Usage
Run the Streamlit app locally:

```bash
Copy code
streamlit run app.py
Sidebar Options:

Upload FASTA file: Upload .fasta or .fa file containing protein sequence.

Manual input: Paste amino acid sequence directly.

Visualization style: Select Cartoon (ribbon) or Stick (atomic stick representation).

Spin structure: Enable/disable rotation.

Predict: Generate the protein structure.

Output:

Interactive 3D protein structure

Downloadable predicted.pdb file for downstream analysis

Note: Long sequences (>400 residues) may timeout on the ESMFold API.

Folder Structure
│
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── utils/
│   ├── __init__.py
│   ├── fasta.py            # FASTA parsing utility
│   ├── esmfold_api.py      # ESMFold API functions
│   └── visualization.py    # Protein rendering functions
└── README.md


##  Contributing
Contributions are welcome! You can:

Add new visualization features (e.g., surface view)

Improve error handling or caching

Optimize performance for long sequences

Please fork the repository, create a branch for your changes, and submit a pull request.



## Disclaimer

This tool uses a public API. Prediction speed and availability depend on the ESMFold service.
