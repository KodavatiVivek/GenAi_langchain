import sys
from pathlib import Path
from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_pdfs() -> list[Document]:
    try:
        backend_dir = Path(__file__).resolve().parents[2]
        data_dir = backend_dir / "data"

        loader = PyPDFDirectoryLoader(str(data_dir))
        documents = loader.load()

        logger.info(f"Loaded {len(documents)} pages from {data_dir}")
        return documents

    except Exception as e:
        logger.error(str(e))
        raise CustomException(e, sys)
