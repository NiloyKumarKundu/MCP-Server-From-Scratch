import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

nest_asyncio.apply()  # Needed to run interactive python

"""
Make sure:
1. The server is running before running this script. (7.Build_Expense_Tracker_SSE_Server.py)
2. The server is configured to use SSE transport.
3. The server is listening on port 8000.

To run the server:
uv run 7.Build_Expense_Tracker_SSE_Server.py
"""


async def main():
    # Connect to the server using SSE
    async with sse_client("https://expense-tracker-by-niloy.fastmcp.app/mcp") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Call our Expense Tracker tool
            result = await session.call_tool("add_expense", 
                                             arguments={
                                                "date": "2025-10-14",
                                                "note": "Buy a Matador High School Pen",
                                                "amount": 6,
                                                "category": "Stationary",
                                                "subcategory": ""
                                             })
            print(f"Response = {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
