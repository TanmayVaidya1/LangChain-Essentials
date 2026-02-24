from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

parser = JsonOutputParser()

template = PromptTemplate.from_template(
    """
    Explain {topic}.
    Return output in JSON format with keys:
    definition, example
    """
)

chain = template | llm | parser

response = chain.invoke({"topic": "Embeddings"})

print(response)
print(type(response))
