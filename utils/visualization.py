import py3Dmol
from stmol import showmol

def render_mol(pdb_string: str, style: str = "cartoon", spin: bool = True):
    """
    Render a protein structure in Streamlit with Py3Dmol.
    Only Cartoon or Stick style, with optional spinning.
    """
    view = py3Dmol.view()
    view.addModel(pdb_string, "pdb")

    rep = "stick" if style.lower() == "stick" else "cartoon"

    # Base representation (simple, no plDDT coloring)
    view.setStyle({rep: {"color": "spectrum"}})

    view.setBackgroundColor("white")
    view.zoomTo()
    view.zoom(2, 800)

    if spin:
        view.spin(True)

    showmol(view, height=500, width=800)
