from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load environment variables (must include GOOGLE_API_KEY)
load_dotenv()

# Create embedding object with Gemini 1.5 Flash
embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"  # Embedding endpoint, not the chat model
)

# Embed a query
result = embedding.embed_query("Delhi is the capital of India")

print(str(result))
