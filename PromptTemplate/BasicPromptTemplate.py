from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = PromptTemplate.from_template(
    "Explain {topic} in 3 bullet points"
)

prompt = template.format(topic="Vector Database")

response = llm.invoke(prompt)

print(response.content)
