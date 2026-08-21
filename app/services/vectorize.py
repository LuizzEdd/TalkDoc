from core.config import settings
from core.llms import embedding_model
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pymupdf

def process_pdf(pdf_path, collection_name: str) -> None:

    doc = pymupdf.open(pdf_path)

    paginas = []
    documents = []

    for page in doc:
        paginas.append({
            "page": page.number + 1,
            "text": page.get_text()
    })

    for page in paginas:
            document = Document(
                page_content = page["text"],
                metadata = {"page": page["page"]},
            )
            documents.append(document)
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100
    )

    chunks = splitter.split_documents(documents)
    
    ids = [f"page_{chunk.metadata['page']}_chunk_{i}" for i, chunk in enumerate(chunks)]

    vector_store = Chroma(
        collection_name=collection_name,
        persist_directory=settings.CHROMA_DIR,
        embedding_function=embedding_model
    )
    
    vector_store.add_documents(documents=chunks, ids=ids)

def get_retriever(collection_name: str):
    vector_store = Chroma(
             collection_name=collection_name,
             persist_directory=settings.CHROMA_DIR,
             embedding_function=embedding_model
    )
    return vector_store.as_retriever(
        search_kwargs={"k": settings.TOP_K}
    )