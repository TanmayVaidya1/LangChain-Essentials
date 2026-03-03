from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv

load_dotenv()

# Load LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# 🔥 Keep only last 5 exchanges
memory = ConversationBufferWindowMemory(
    k=5,              # last 5 exchanges
    return_messages=True
)

# Create Conversation Chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True   # shows prompt being sent to LLM
)

# Conversation
conversation.predict(input="Hi, my name is Tanmay.")
conversation.predict(input="I am learning LangChain.")
conversation.predict(input="I like building chat apps.")
conversation.predict(input="I am working with Kafka.")
conversation.predict(input="I use MongoDB.")
conversation.predict(input="I also use React.")

# Ask memory question
response = conversation.predict(input="What is my name?")
print("\nFinal Response:", response)

# 🔥 Print Buffer
print("\n--- Current Memory Buffer ---")
for msg in memory.chat_memory.messages:
    print(f"{msg.type.upper()}: {msg.content}")