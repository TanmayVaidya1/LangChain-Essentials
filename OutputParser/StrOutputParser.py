from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

template = PromptTemplate.from_template(
    "Explain {topic} in 2 lines."
)

parser = StrOutputParser()

chain = template | llm | parser

response = chain.invoke({"topic": "LangChain"})

print(response)
