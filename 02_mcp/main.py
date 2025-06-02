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
async def get_weather_data(city: str):
    """
    Get weather data for any city.

    Args:
        city: The name of the city to get weather info for.
    """
    weather = await get_weather_by_city(city)
    return weather

if __name__ == "__main__":
    # Run the FastMCP server
    mcp.run(transport="stdio")
