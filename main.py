import os  # for environment variable handling
import asyncio  # for asynchronous programming
from pydantic_ai import Agent  # import AI agent
from pydantic_ai.mcp import MCPServerStdio  # MCP server over stdio
from dotenv import load_dotenv  # to load .env file

# Load environment variables from .env
load_dotenv()
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")# Set GROQ API key

# Define MCP server to fetch data (used for tools like browser, code, etc.)
mcp_fetch_server = MCPServerStdio(
    command="python",
    args=["-m", "mcp_server_fetch"]
)

# Initialize AI agent with model and MCP tools
# agent = Agent(
#     model="groq:llama-3.3-70b-versatile",  # specify model
#     mcp_servers=[mcp_fetch_server]  # attach the fetch tool
# )

agent = Agent(
    model="gpt-4o",  # specify model
    mcp_servers=[mcp_fetch_server]  # attach the fetch tool
)

# Define the main async function to run the agent
async def main(prompt):
    async with agent.run_mcp_servers():  # start MCP tool servers
        result = await agent.run( 
            "https://www.cricbuzz.com/live-cricket-scores/105780/ind-vs-eng-5th-test-india-tour-of-england-2025")
        return result.output  # return final response


# Run the async main function
if __name__ == "__main__":
    prompt = "extract the content and tell me the bowelers economy in table"
    output = asyncio.run(main(prompt))  # run event loop
    print(output)  # print result
