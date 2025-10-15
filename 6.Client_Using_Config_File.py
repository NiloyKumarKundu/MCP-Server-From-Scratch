import asyncio
from langchain_groq import ChatGroq
import os
from mcp_use import MCPAgent, MCPClient
from dotenv import load_dotenv

async def run_memory_chat():
    """Run a chat using MCPAgent's build-in conversation memory."""
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    config_file = os.path.join(os.path.dirname(__file__), "config", "expense_tracker.json")
    print("Initializing chat...")
    
    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="openai/gpt-oss-20b")
    
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True
    )
    
    print("\n===== Chat started =====\n")
    
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Exiting chat...")
                break
            
            if user_input.lower() in ["clear", "reset"]:
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue
            
            print("\nAssistant: ", end="", flush=True)
            
            try:
                response = await agent.run(user_input)
                print(response)
            except Exception as e:
                print(f"\nError: {e}")
    except KeyboardInterrupt:
        print("\n===== Chat ended =====\n")
    finally:
        if client and client.sessions:
            await client.close_all_sessions()
    
    
if __name__ == "__main__":
    asyncio.run(run_memory_chat())