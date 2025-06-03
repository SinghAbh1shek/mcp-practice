import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def run():
    async with sse_client(url = "http://127.0.0.1:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            tools = await session.list_tools()
            print('tool_name: ', (tools.tools[0].name))

            result = await session.call_tool("get_weather_for_city", arguments = {'city': 'Jaipur'})
            print((result.content[0].text))

if __name__ == '__main__':
    asyncio.run(run())