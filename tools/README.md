
# Agentic RAG Leave Policy Chatbot

An **end-to-end Agentic RAG chatbot** that answers company leave policy questions using **document grounding**, **role-based rules**, and **dynamic response styles** (short vs detailed).
Built with **LangGraph**, **Gemini**, **FAISS**, **FastAPI**, and a custom **HTML/CSS/JS frontend with login**.

---
### ✨ Features

This project implements an **Agentic RAG architecture** using LangGraph, where a state-based agent orchestrates retrieval and reasoning through dedicated tools such as a document retriever and a role-based API. The system provides **document-grounded answers** by leveraging company leave policy documents, holiday calendars, and intern-specific rules to ensure accurate and context-aware responses.

The chatbot supports **role-based logic**, differentiating behavior and answers for interns, employees, and managers. It also includes **dynamic response styling**, automatically generating concise answers for simple queries and detailed, structured explanations for policy-related or explanatory questions.

Conversation context is preserved using **LangGraph-managed state memory**, enabling coherent multi-turn interactions. The backend is exposed through a **FastAPI service**, making the system easily deployable and extensible.

A **custom web-based frontend** built with HTML, CSS, and JavaScript provides a login interface (demo-based ID and password) and an interactive chat experience. The overall solution is **cost-efficient**, utilizing local HuggingFace embeddings for retrieval while relying on Gemini models exclusively for reasoning.

---

## 🏗️ Architecture Overview

```
Frontend (HTML/CSS/JS)
        |
        |  POST /ask
        v
FastAPI Backend
        |
        v
LangGraph Agent
  ├─ Retrieve Docs (FAISS + HF embeddings)
  ├─ Apply Role Rules
  ├─ Decide Response Style
  └─ Gemini LLM (Reasoning)
```

---

## 📁 Project Structure

```
agentic_RAG_leave_policy/
│
├── app.py                # FastAPI app
├── graph.py              # LangGraph agent
├── tools/
│   ├── retriever.py      # FAISS retriever
│   └── api_tool.py       # User role lookup
├── data/
│   └── leave_policy.txt  # Policy documents
├── faiss_db/             # Vector store
├── frontend/
│   ├── index.html        # Login page
│   ├── chat.html         # Chat UI
│   ├── style.css
│   └── script.js
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Tech Stack

* **LLM**: Gemini (`gemini-2.5-flash`)
* **Agent Framework**: LangGraph
* **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)
* **Vector DB**: FAISS
* **Backend**: FastAPI
* **Frontend**: HTML, CSS, JavaScript

---

## 🔑 Environment Setup

### Create `.env`

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Ingest documents

```bash
python ingest.py
```

---

## Run the Application

### Start backend

```bash
uvicorn app:app --reload
```

* Swagger UI:
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### Open frontend

```
frontend/index.html
```

Login with:

* **User ID**: `101` (employee) or `102` (intern)
* **Password**: any (demo only)

---

## 💬 Example Queries

### Short response

**Question:**

> Can I take 10 days leave?

**Answer:**

> No. As an intern, you are allowed a maximum of 5 days of leave.

---

### Detailed response

**Question:**

> What is the employee leave policy?

**Answer:**

* Employees are entitled to 20 days of annual leave
* Manager approval is mandatory
* Public holidays are separate from annual leave
* Leave carry-forward is subject to HR approval

---

### Response Style Logic

The agent automatically adjusts verbosity:

* **Short** → simple questions (“can I”, “how many days”)
* **Detailed** → “policy”, “explain”, “rules”, “process”

This is handled inside the **LangGraph agent prompt**, not the UI.

---

