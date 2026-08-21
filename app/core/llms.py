from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from core.config import settings

chat_model = ChatGoogleGenerativeAI(
    model=settings.CHAT_MODEL,
    google_api_key=settings.GEMINI_API_KEY
)

embedding_model = GoogleGenerativeAIEmbeddings(
    model=settings.EMBEDDING_MODEL,
    google_api_key=settings.GEMINI_API_KEY
)

RAG_TEMPLATE = """
Você é um assistente de IA que responde perguntas com base exclusivamente
no conteúdo dos documentos fornecidos.

Use apenas as informações presentes no contexto.

Se a resposta não estiver presente no contexto, diga claramente que
não foi possível encontrar essa informação nos documentos.

Contexto:
{documents}

Pergunta:
{question}

Responda de forma clara e objetiva.
"""

rag_prompt = ChatPromptTemplate.from_template(RAG_TEMPLATE)
rag_chain = rag_prompt | chat_model