from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.6
)

response = llm.invoke("Explain LangChain in simple words.")
print(response.content)
