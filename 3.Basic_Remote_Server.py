from fastmcp import FastMCP
import random
import json
import datetime

mcp = FastMCP(name="Simple Remote Server")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b

@mcp.tool 
def random_number(min: int, max: int) -> int:
    """Generate a random number between min and max"""
    return random.randint(min, max)

@mcp.resource("info://server")
def server_info() -> str:
    """Get server information"""
    info = {
        "name": "Simple Remote Server",
        "version": "1.0.0",
        "description": "A simple remote server with math tools",
        "tools": ["add", "random_number"],
        "author": "Niloy Kumar Kundu",
        "email": "niloykk.connect@gmail.com",
        "timestamp": datetime.datetime.now().isoformat()
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000) # Main changes are here