from mcp.server.fastmcp import FastMCP
import httpx

# Initialize FastMCP server
mcp = FastMCP("weather")


async def get_weather_by_city(city: str) -> str:
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = httpx.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return "Something went wrong"



@mcp.tool()
async def get_weather_for_city(city: str):
    """
    Gets the weather information for a city.

    Args:
        city: The name of the city to get the weather for.
    """

    weather = await get_weather_by_city(city)
    return weather

if __name__ == "__main__":
    mcp.run(transport="sse")
