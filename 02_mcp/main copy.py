from mcp.server.fastmcp import FastMCP
from typing import Any

# Initialize FastMCP server
mcp = FastMCP("weather")


def get_weather_by_city(city: str) -> dict[str, Any]:
    city = city.lower()
    if city == "sasaram":
        return {"temp": "30C", "forecast": "chances for high rain"}
    elif city == "patna":
        return {"temp": "45C", "forecast": "chances of high warm winds"}
    else:
        return {"temp": None, "error": "Unable to get the details"}



@mcp.tool()
def get_weather_datas(city: str):
    """
    Get weather data for any city.

    Args:
        city: The name of the city to get weather info for.
    """
    weather = get_weather_by_city(city)
    return weather

if __name__ == "__main__":
    # Run the FastMCP server
    mcp.run(transport="stdio")
