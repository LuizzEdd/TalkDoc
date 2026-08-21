from core.llms import rag_chain
from services.vectorize import get_retriever

def ask_question(collection_name: str, question: str) -> dict:
    retriever = get_retriever(collection_name)
    documents = retriever.invoke(question)
    context = "\n\n".join(
        [
            f"Página {doc.metadata['page']}:\n{doc.page_content}"
            for doc in documents
        ]
        )
    result = rag_chain.invoke({"documents": context, "question": question})
    return {
        "answer": result.text,
        "sources": [f"Página(s) {doc.metadata['page']}" for doc in documents]
    }