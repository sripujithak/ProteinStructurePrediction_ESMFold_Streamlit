# ESMFold Protein Structure Predictor

**ESMFold Streamlit App** is an interactive web application designed to predict and visualize protein 3D structures from amino acid sequences. It leverages the ESMFold model (ESM-2) via the ESM Atlas API for high-accuracy predictions without requiring local heavy-duty computing resources.

---

## ⚡ Features

- **Flexible Input:** Predict structures from **FASTA file uploads** or **manual sequence entry**.
- **Interactive 3D Visualization:** Powered by [stmol] and [py3Dmol]. 
    - Toggle between **Cartoon** (ribbon) or **Stick** representations.
    - Enable **Spin toggle** for dynamic rotation.
- **Export Capabilities:** Download the predicted structure as a `.pdb` file for downstream analysis in software like PyMOL or ChimeraX.
- **Modern UI:** Simple, responsive interface built entirely with Streamlit.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/esmfold-streamlit.git](https://github.com/yourusername/esmfold-streamlit.git)
   cd esmfold-streamlit
Install dependencies:

Bash

pip install -r requirements.txt
🚀 Usage
Run the Streamlit app locally with the following command:

Bash

streamlit run app.py
Sidebar & Settings
Upload FASTA file: Supports .fasta or .fa files.

Manual Input: Paste raw amino acid sequences directly into the text area.

Visualization Style: * Cartoon: Best for viewing secondary structures (alpha-helices, beta-sheets).

Stick: Best for viewing atomic-level detail and side chains.

Spin Structure: Toggle to keep the protein in constant motion.

Predict Button: Triggers the API call to ESMFold.

📂 Project Structure



├── app.py                  # Main Streamlit application entry point
├── requirements.txt        # Python dependencies
├── utils/
│   ├── __init__.py
│   ├── fasta.py            # FASTA parsing and validation utility
│   ├── esmfold_api.py      # ESMFold API request handling
│   └── visualization.py    # Protein rendering and stmol configurations
└── README.md
Important Notes
Sequence Limits: The ESMFold API typically has a limit for long sequences (often >400 residues). Sequences exceeding this may result in a timeout or error.

Internet Connection: An active internet connection is required to communicate with the ESM Atlas API.

Contributing
Contributions make the open-source community an amazing place to learn and create. Any contributions you make are greatly appreciated.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

Suggested Improvements:

[ ] Add Surface View visualization.

[ ] Implement caching to prevent re-running the same sequence multiple times.

[ ] Add pLDDT (confidence) color coding to the 3D model.