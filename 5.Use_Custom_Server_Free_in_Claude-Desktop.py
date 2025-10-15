"""
How to Use Custom MCP Servers in Claude Desktop

This file demonstrates how to configure and use custom MCP servers
in Claude Desktop for free, without any paid subscriptions.


After run this file, you can use the custom server in Claude Desktop by using the following command:

```
uv run fastmcp install claude-desktop 5.Use_Custom_Server_Free_in_Claude-Desktop.py
```
"""

from fastmcp import FastMCP

# Create a proxy to your remote FastMCP Cloud server
# FastMCP cloud uses Streamable HTTP (default), so just use the /mcp URL

mcp = FastMCP.as_proxy(
    "https://expense-tracker-by-niloy.fastmcp.app/mcp",    # URL of the remote server
    name="Expense Tracker",
)

if __name__ == "__main__":
    # This runs via STDIO, which Claude Desktop uses for communication
    mcp.run() 
    
