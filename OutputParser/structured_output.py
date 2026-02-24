from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class TopicResponse(BaseModel):
    definition: str
    example: str

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

structured_llm = llm.with_structured_output(TopicResponse)

result = structured_llm.invoke(
    "Explain what a Vector Database is."
)

print(result)
print(type(result))
