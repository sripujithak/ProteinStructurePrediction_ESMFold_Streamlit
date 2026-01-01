ESMFold Streamlit App
This application provides a user-friendly web interface for predicting protein structures using the ESMFold API and visualizing them in 3D.

🚀 Installation
Follow these steps to set up the project locally:

Bash

# Clone the repository
git clone https://github.com/yourusername/esmfold-streamlit.git

# Navigate to the directory
cd esmfold-streamlit

# Install dependencies
pip install -r requirements.txt
🛠 Usage
To launch the application, run the following command in your terminal:

Bash

streamlit run app.py
Sidebar Options
Upload FASTA file: Upload .fasta or .fa files containing your protein sequence.

Manual input: Paste amino acid sequences directly into the text area.

Visualization style: Choose between Cartoon (ribbon) or Stick (atomic representation).

Spin structure: Toggle automatic rotation of the 3D model.

Predict: Click this button to generate the protein structure.

Output
Interactive 3D protein structure: Explore the predicted model directly in your browser.

Downloadable PDB file: Export the predicted.pdb file for use in downstream analysis (e.g., PyMOL, ChimeraX).

[!NOTE] Long sequences (typically >400 residues) may experience timeouts due to limitations of the public ESMFold API.

📂 Folder Structure
Plaintext

│
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── utils/
│   ├── __init__.py
│   ├── fasta.py            # FASTA parsing utility
│   ├── esmfold_api.py      # ESMFold API functions
│   └── visualization.py    # Protein rendering functions
└── README.md
🤝 Contributing
Contributions are welcome! If you'd like to help improve this tool, consider:

Adding new visualization features (e.g., surface view or pLDDT coloring).

Improving error handling and response caching.

Optimizing performance for longer sequences.

To contribute: Fork the repository, create a branch for your changes, and submit a pull request.

⚖️ Disclaimer
This tool utilizes a public API. Prediction speed and service availability are dependent on the ESMFold external service provider.