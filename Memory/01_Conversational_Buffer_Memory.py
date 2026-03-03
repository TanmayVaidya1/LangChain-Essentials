from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# Conversation
chain_with_memory.invoke(
    {"input": "Hi, my name is Tanmay."},
    config={"configurable": {"session_id": "1"}}
)

chain_with_memory.invoke(
    {"input": "What is my name?"},
    config={"configurable": {"session_id": "1"}}
)

# 🔥 Print buffer
print("\n--- Conversation Buffer ---")
for message in store["1"].messages:
    print(f"{message.type.upper()}: {message.content}")