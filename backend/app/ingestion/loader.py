from langchain_community.document_loaders import PyPDFDirectoryLoader

loader = PyPDFDirectoryLoader("data/")  
documents = loader.load()
print(f"✅ Loaded: {len(documents)} pages")


