from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# Step 1: Define Schema
class TopicResponse(BaseModel):
    definition: str
    example: str

# Step 2: Create parser
parser = PydanticOutputParser(pydantic_object=TopicResponse)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

template = PromptTemplate.from_template(
    """
    Explain {topic}.
    {format_instructions}
    """
)

# Inject format instructions automatically
prompt = template.partial(format_instructions=parser.get_format_instructions())

chain = prompt | llm | parser

result = chain.invoke({"topic": "Vector Database"})

print(result)
print(type(result))

print(result.definition)
