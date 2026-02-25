from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
parser = StrOutputParser()

# Prompt 1: Restaurant Name
template_restaurant_name = PromptTemplate.from_template(
    "I want to open a restaurant for {cuisine} food. "
    "Suggest a fancy name. Only one name please."
)

# Prompt 2: Menu Items
template_menu_items = PromptTemplate.from_template(
    "Suggest some menu items for {restaurant_name}. "
    "Return as comma-separated list."
)

# Chain to generate restaurant name
restaurant_name_chain = template_restaurant_name | llm | parser

# Full chain
chain = (
    {"restaurant_name": restaurant_name_chain}  # Step 1
    | RunnablePassthrough.assign(              # Step 2
        menu_items=(
            template_menu_items
            | llm
            | parser
        )
    )
)

# Invoke
response = chain.invoke({"cuisine": "Indian"})

# Extract variables
restaurant_name = response["restaurant_name"]
menu_items = response["menu_items"]

print("Restaurant Name:", restaurant_name)
print("Menu Items:", menu_items)