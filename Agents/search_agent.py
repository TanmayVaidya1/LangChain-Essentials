from langchain.agents import create_react_agent, AgentExecutor, load_tools
from langchain import hub
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)

# 🔥 Add llm-math tool here
tools = load_tools(["serpapi"], llm=llm)

#prompt
prompt = hub.pull("hwchase17/react")

# Create agent
agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)
result = agent_executor.invoke({
    "input": "What is the population of New York City in 2023? What will be the population in 2026 if it grows at a rate of 1.5% per year?"
})

print(result["output"])