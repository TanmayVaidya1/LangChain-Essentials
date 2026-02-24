from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5
)

# Create prompt template
template = PromptTemplate.from_template(
    "Explain {topic} in simple words."
)

# Create output parser
parser = StrOutputParser()

# Create chain
chain = template | llm | parser

# Invoke chain
response = chain.invoke({"topic": "RAG"})

print(response)