import sys
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .loader import load_pdfs
from ..utils.exception import CustomException
from ..utils.logger import logger


def split_documents():
    try:
        documents = load_pdfs()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150,
            separators=["\n\n", "\n", ".", " ", ""]
        )

        chunks = splitter.split_documents(documents)
        if chunks:
            logger.info(f"✅ Split into {len(chunks)} chunks")
            logger.info(f"Sample chunk: {chunks[0].page_content[:200]}...")  # Log a sample chunk
            return chunks

    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    split_documents()