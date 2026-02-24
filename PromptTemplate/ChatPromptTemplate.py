from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Explain {topic} in 3 bullet points"),
    ]
)

prompt = prompt.format_messages(topic="Vector Database")
response = llm.invoke(prompt)

print(response.content)
