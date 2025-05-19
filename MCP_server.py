import math
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

@mcp.tool()
def sine(a: int) -> float:
    return math.sin(a)

WEATHER_API_KEY = "3eb492a34cd8482fb8c120039251705"

@mcp.tool()
def get_weather(city: str) -> dict:
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": f"Failed to fetch weather for {city}."}
    data = response.json()
    return {
        "city": data["location"]["name"],
        "region": data["location"]["region"],
        "country": data["location"]["country"],
        "temperature_C": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"]
    }

if __name__ == "__main__":
    print("Starting MCP Server...")
    mcp.run(transport="stdio")
