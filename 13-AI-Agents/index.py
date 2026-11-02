
import os
import requests

from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun


# 1. Initialize the LLM
model = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)


# 2. Initialize search tool
search_tool = DuckDuckGoSearchRun()


# 3. Create custom weather tool
@tool
def get_weather_data(city: str) -> str:
    """Fetch current weather conditions for a given city."""

    # Find city coordinates
    geo_response = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1},
        timeout=10
    )
    geo_response.raise_for_status()

    locations = geo_response.json().get("results", [])

    if not locations:
        return f"Could not find location: {city}"

    location = locations[0]

    # Fetch current weather
    weather_response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
            "timezone": "auto"
        },
        timeout=10
    )
    weather_response.raise_for_status()

    weather = weather_response.json()["current"]

    return str({
        "city": location["name"],
        "temperature": weather["temperature_2m"],
        "feels_like": weather["apparent_temperature"],
        "humidity": weather["relative_humidity_2m"],
        "precipitation": weather["precipitation"],
        "wind_speed": weather["wind_speed_10m"],
        "weather_code": weather["weather_code"],
        "time": weather["time"]
    })


# 4. Register tools
tools = [
    search_tool,
    get_weather_data
]


# 5. Create agent
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
    You are a helpful assistant.

    Use the available tools whenever external information
    or current weather information is required.

    Provide accurate and concise answers.
    """
)


# 6. Invoke agent
response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Find the capital of Madhya Pradesh, then find it's current weather condition"
        }
    ]
})


for message in response["messages"]:
    print("\nMessage type:", type(message).__name__)
    print("Content:", message.content)

    if hasattr(message, "tool_calls") and message.tool_calls:
        print("Tool calls:", message.tool_calls)
