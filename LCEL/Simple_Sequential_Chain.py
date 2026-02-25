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

# Create output parser
parser = StrOutputParser()

# Prompt 1: Restaurant Name
template_restaurant_name = PromptTemplate.from_template(
    "I want to open a restaurant for {cuisine} food. "
    "Suggest a fancy name for this. Only one name please."
)

# Prompt 2: Menu Items
template_menu_items = PromptTemplate.from_template(
    "Suggest some menu items for {restaurant_name}. "
    "Return it as a comma-separated list."
)

# Chain 1
restaurant_name_chain = template_restaurant_name | llm | parser

# Chain 2
menu_items_chain = template_menu_items | llm | parser

# Sequential chaining (NEW STYLE)
chain = (
    restaurant_name_chain
    | (lambda name: {"restaurant_name": name})
    | menu_items_chain
)

# Invoke
response = chain.invoke({"cuisine": "Italian"})

print(response)