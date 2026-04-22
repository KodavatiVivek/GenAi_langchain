from langchain_huggingface import HuggingFaceEmbeddings
from app.config import hf_token
from app.utils.logger import get_logger
from .loader import load_documents
from .splitter import split_documents


logger = get_logger(__name__)


def get_embedding_model(chunks):
    try:
        logger.info("Loading embedding model...")
        
        model_name = "sentence-transformers/all-MiniLM-L6-v2"

        embeddings_model = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs={"device": "cpu", "token": hf_token},
            encode_kwargs={"normalize_embeddings": True}
        )
        text = "This is a test sentence"
        vector =embeddings_model.embed_query(text)
        logger.info(f"Test embedding vector: {vector[:5]}...")  # Log the first 5 dimensions of the embedding
        logger.info(f"Embedding model loaded successfully: {model_name}")
        return embeddings_model
        

    except Exception as e:
        logger.error(f"Error loading embedding model: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    documents = load_documents()
    chunks = split_documents(documents)
    embedding_model = get_embedding_model(chunks)