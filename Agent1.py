from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os
import logging
import requests


load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Wiki search tool
def Wiki_search(query):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('extract', 'No information found')
        else:
            return f"Error: Wikipedia returned status code {response.status_code}"
    except Exception as e:
        logging.error(f"Something went wrong on wiki search: {e}")
        return "Error during Wikipedia search."

# Setup LLM
llm = ChatOpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0,
    model='gpt-3.5-turbo'
)

# Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Tool
tool = Tool(
    name="Wikipedia",
    func=Wiki_search,
    description="Search Wikipedia for information."
)

template = """
You are a helpful conversational assistant with access to tools.
You can remember our conversation and use tools when needed.

Previous conversation:
{chat_history}

Available tools:
{tool_names}

Tools details:
{tools}

Use this format:
Question: {input}
Thought: What should I do?
Action: [tool name]
Action Input: [input to tool]
Observation: [result from tool]
Thought: I now know what to respond
Final Answer: [response to human]

Question: {input}
Thought: {agent_scratchpad}
"""

# PromptTemplate must match exactly
prompt_template = PromptTemplate(
    template=template,
    input_variables=["input", "agent_scratchpad", "tools", "tool_names", "chat_history"]
)

# Agent
agent = create_react_agent(
    llm=llm,
    tools=[tool],
    prompt=prompt_template
)

# Executor
executor = AgentExecutor(
    agent=agent,
    tools=[tool],
    memory=memory,
    verbose=True
)

# Run
response = executor.invoke({"input": "Who won the football world cup in 2022?"})

print(response['output'])
