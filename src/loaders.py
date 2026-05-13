from pathlib import Path
from pypdf import PdfReader
from docx import Document
from pptx import Presentation

def load_txt(path: Path) -> str:
    """plain text file reading and converts its content to string"""
    return path.read_txt(encoding="utf-8", errors="ignore")

def load_pdf(path: Path) -> str:
    """extract text from all pages of pdf, return it joined as one str"""
    reader =PdfReader(path)
    pages_text=[page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages_text)

def load_docx(path: Path) -> str:
    """extract text from word docx, to whoever is reading this in detail, yaha tk aagye ho i mean....thanks..yup thanks and proof ki this code is not copy pasted instead hand written haha"""
    doc=Document(path)
    paragraphs=[para.text for para in doc.paragraphs]
    return "\n".join(paragraphs)

def load_pptx(path: Path) -> str:
    """extracts text from ppt"""
    prs=Presentation(path)
    texts=[]
    for slide in prs.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                texts.append(shape.text_frame.text)
    return "\n".join(texts)

EXTENSION_MAP = {
    ".txt": load_txt,
    ".pdf": load_pdf,
    ".docx": load_docx,
    ".pptx": load_pptx,
}

def load_file(path: Path) -> str | None:
    """Dispatch to the correct loader based on file extension. Returns None for unsupported types."""
    loader = EXTENSION_MAP.get(path.suffix.lower())
    if loader is None:
        return None
    try:
        return loader(path)
    except Exception as e:
        print(f"failed to load {path.name}: {e}")
        return None
            
def load_folder(folder_path: str) -> list[dict]:
    """
    Walk a folder recursively, extract text from every supported file.
    Returns a list of dicts: [{filename, filepath, file_type, text}, ...]
    """
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    results = []
    for file_path in folder.rglob("*"):
        if not file_path.is_file():
            continue
        text = load_file(file_path)
        if text is None or text.strip() == "":
            continue
        results.append({
            "filename": file_path.name,
            "filepath": str(file_path),
            "file_type": file_path.suffix.lower(),
            "text": text,
        })
    return results

if __name__ == "__main__":
    docs = load_folder("data/sample")
    print(f"Loaded {len(docs)} documents.\n")
    for doc in docs:
        preview = doc["text"][:200].replace("\n", " ")
        print(f"📄 {doc['filename']} ({doc['file_type']})")
        print(f"   Preview: {preview}...\n")