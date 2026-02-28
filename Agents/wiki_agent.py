from langchain.agents import create_react_agent, AgentExecutor, load_tools
from langchain import hub
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)

# 🔥 Add llm-math tool here
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# ReAct prompt
prompt = hub.pull("hwchase17/react")

# Create agent
agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

result = agent_executor.invoke({
    "input": "When was Elon Musk born? What is his age in 2026?"
})

print(result["output"])