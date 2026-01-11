from typing import TypedDict, List
from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.retriever import retrieve_docs
from tools.api_tool import get_user_role


# -------------------------
# Gemini LLM
# -------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


# -------------------------
# LangGraph State (THIS IS MEMORY)
# -------------------------
class AgentState(TypedDict):
    question: str
    user_id: str
    chat_history: List[str]
    answer: str


# -------------------------
# Agent Node
# -------------------------
def agent_node(state: AgentState) -> AgentState:
    question = state["question"]
    user_id = state["user_id"]
    chat_history = state.get("chat_history", [])

    role = get_user_role(user_id)
    context = retrieve_docs(question)

    prompt = f"""
You are an HR assistant.

Previous conversation:
{chat_history}

User role: {role}

Rules:
- Interns can take a maximum of 5 days leave
- Employees can take up to 20 days leave
- Managers require approval

Context:
{context}

Question:
{question}

Answer clearly and follow the rules.
"""

    result = llm.invoke(prompt)
    answer = result.content if hasattr(result, "content") else result

    # ✅ Update memory
    chat_history.append(f"Q: {question}")
    chat_history.append(f"A: {answer}")

    return {
        "question": question,
        "user_id": user_id,
        "chat_history": chat_history,
        "answer": answer
    }


# -------------------------
# Build LangGraph
# -------------------------
graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")
graph.set_finish_point("agent")

app = graph.compile()
