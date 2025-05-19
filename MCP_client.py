from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import uvicorn
import asyncio
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

# Setup environment
GROQ_API_KEY = "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"
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# LangChain model
model = ChatGroq(model="llama3-8b-8192", temperature=0)

# MCP server script
server_params = StdioServerParameters(command="python", args=["MCP_server.py"])

app = FastAPI()

# HTML form for input and output display
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>MCP Localhost UI</title>
</head>
<body>
    <h2>Ask something...</h2>
    <form method="post">
        <input type="text" name="query" style="width: 300px;" required/>
        <button type="submit">Submit</button>
    </form>
    {result}
</body>
</html>
"""

# Global async lock for agent reuse
agent_lock = asyncio.Lock()

@app.get("/", response_class=HTMLResponse)
async def home():
    return html_form.format(result="")

@app.post("/", response_class=HTMLResponse)
async def handle_query(query: str = Form(...)):
    async with agent_lock:  # Prevent overlapping agent sessions
        try:
            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    tools = await load_mcp_tools(session)
                    agent = create_react_agent(model, tools)
                    response = await agent.ainvoke({
                        "messages": [{"role": "user", "content": query}]
                    })
                    answer = response["messages"][-1].content
                    return html_form.format(result=f"<h3>Response:</h3><p>{answer}</p>")
        except Exception as e:
            return html_form.format(result=f"<p style='color:red;'>Error: {str(e)}</p>")

# Entry point
if __name__ == "__main__":
    uvicorn.run("MCP_client:app", host="127.0.0.1", port=8001, reload=False)
