from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3-pro-preview')

result = model.invoke('what is gen ai?')

print(result.content)