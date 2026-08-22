from core.llms import rag_chain
from services.vectorize import get_retriever


def extract_text(message) -> str:
    content = message.content
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
            elif isinstance(block, str):
                parts.append(block)
        return "".join(parts)
    return str(content)

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

    pages = sorted(set(doc.metadata['page'] for doc in documents))
    sources = [f"Página {p}" for p in pages]

    return {
        "answer": extract_text(result),
        "sources": sources
    }