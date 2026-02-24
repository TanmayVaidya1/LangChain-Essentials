from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

parser = CommaSeparatedListOutputParser()

template = PromptTemplate.from_template(
    "Give 5 programming languages separated by commas."
)

chain = template | llm | parser

result = chain.invoke({})

print(result)
print(type(result))
