import asyncio
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

"""Simple test client."""


async def main():
    # transport = StdioTransport(command="uv", args=["run", "dicom-knowledge-mcp/server.py"])
    transport = StdioTransport(command="uvx", args=["dicom-knowledge-mcp"])

    # Connect via stdio to a local script
    async with Client(transport) as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")
        result = await client.call_tool(
            "search_dicom_standard", {"query": "What are dicoms for?"}
        )
        print(f"Result: {result.content}")


asyncio.run(main())
