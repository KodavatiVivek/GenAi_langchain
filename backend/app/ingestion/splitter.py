from langchain_text_splitters import RecursiveCharacterTextSplitter
from .loader import load_documents
from app.utils.logger import get_logger

logger = get_logger(__name__)

def split_documents(documents):
    logger.info("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    logger.info(f"Successfully split documents into {len(chunks)} chunks.")
    return chunks
