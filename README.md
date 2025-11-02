# 🚀 MCP-Based AI Math & Weather Assistant

**Intelligent Agent with Tool Calling via Multi-Component Protocol (MCP)**
*An AI-powered assistant that performs math calculations and fetches real-time weather using a ReAct Agent orchestrating MCP tools — accessible through a simple web UI.*

---

## 📌 Table of Contents

* Demo / Quick Start
* Features
* Tech Stack
* Files in this repo
* Requirements
* Installation & Setup
* How to run
* How it works (high level)
* Environment Variables
* Troubleshooting & Tips
* Security & Privacy
* Future improvements
* Author
* License

---

## 🚀 Demo / Quick Start

1️⃣ Create a virtual environment (recommended)
2️⃣ Install dependencies: `pip install -r requirements.txt`
3️⃣ Add API keys to `.env` file
4️⃣ Run MCP server & client:

```bash
# Terminal 1 → Start MCP Server
python MCP_server.py
```

```bash
# Terminal 2 → Start FastAPI UI Client
python MCP_client.py
```

Open → [http://127.0.0.1:8001](http://127.0.0.1:8001)

Try examples:

* Add 10 and 20
* Weather in Hyderabad
* What is sin(45)?

---

## ✨ Features

* AI Reasoning + Tool Calling (ReAct)
* Math Operations: Add, Multiply, Sine
* Real-time Weather Information
* FastAPI Web User Interface
* Local MCP Tool Server
* Secure Key-based Config

---

## ⚙️ Tech Stack

| Component    | Technology                  |
| ------------ | --------------------------- |
| LLM          | Groq → LLaMA-3-8B-8192      |
| Agent        | LangGraph + LangChain ReAct |
| Tools        | MCP custom tool server      |
| UI           | FastAPI + HTML              |
| Weather Data | WeatherAPI.com              |
| Language     | Python 3.10+                |

---

## 📁 Files in this repo

| File               | Description                              |
| ------------------ | ---------------------------------------- |
| `MCP_server.py`    | MCP server exposing math + weather tools |
| `MCP_client.py`    | FastAPI app interacting with agent + MCP |
| `.env.example`     | Template for environment variables       |
| `requirements.txt` | Python dependencies                      |
| `README.md`        | Project documentation                    |

---

## ✅ Requirements

```
langchain
langchain-core
langgraph
fastapi
uvicorn
python-dotenv
mcp
requests
groq
```

---

## 🛠 Installation & Setup

```bash
git clone <repo-url>
cd <repo>
```

Create & activate venv:

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate
```

Install libs:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create `.env`:

```
GROQ_API_KEY=your_groq_key_here
WEATHER_API_KEY=your_weatherapi_key_here
```

---

## 🧠 How it works (high level)

LLM interprets question → Chooses correct tool → Gets output → Responds back

Tools:

* `add(a,b)`
* `multiply(a,b)`
* `sine(a)`
* `get_weather(city)`

---

## 🧩 Troubleshooting & Tips

| Issue             | Solution                            |
| ----------------- | ----------------------------------- |
| Push rejected     | Use `git pull --rebase` before push |
| Weather error     | Recheck API key & network           |
| Tools not working | Restart both server & client        |

✅ Must run server & client simultaneously

---

## 🔐 Security & Privacy

* API Keys hidden via `.env`
* Data not stored
* Runs locally

---

## 🔮 Future improvements

* Better UI
* More tools: news, currency, calculator
* ReAct improvement
* Deploy MCP with websockets
* Add history + logging

---

## 👨‍💻 Author

**Bhanuji Venkata Teja**

---

## 📜 License

This project is provided as-is. Add MIT for open-source reuse.
