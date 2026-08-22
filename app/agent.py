"""A genuine LangChain agent. The code lane MUST detect this."""
from langchain.agents import AgentExecutor, create_openai_tools_agent
from openai import OpenAI

client = OpenAI()
agent = create_openai_tools_agent(llm=client, tools=[], prompt=None)
executor = AgentExecutor(agent=agent, tools=[])

chatbot: bool = True
