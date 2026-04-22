from langchain_community.document_loaders import PyPDFDirectoryLoader
import os
from app.utils.logger import get_logger

logger = get_logger(__name__)

def load_documents():
 try:
     base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
     data_path = os.path.join(base_dir, "data")
     logger.info(f"Loading documents from: {data_path}")
     loader = PyPDFDirectoryLoader(data_path)
 
     documents = loader.load()
     logger.info(f"Successfully loaded {len(documents)} documents.")
     return documents

 except Exception as e:
     logger.error(f"Error loading documents: {e}")
     return []


    




