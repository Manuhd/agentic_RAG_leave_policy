from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain.agents import initialize_agent
from tools.retriever import retrieve_docs

llm = ChatOpenAI(temperature=0)

search_tool = Tool(
    name="Document Search",
    func=retrieve_docs,
    description="Search company documents"
)

agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)
