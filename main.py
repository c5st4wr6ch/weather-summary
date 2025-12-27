from dotenv import load_dotenv
from weather import get_weather

load_dotenv()

def get_weather_summary():
    weather = get_weather()
    time = weather["localtime"]
    temperature = weather["temp_c"]
    condition = weather["condition"]["text"]

    """Return a weather summary string."""
    return f"Time: {time}, Temperature: {temperature}°C, Condition: {condition}"

if __name__ == "__main__":
    result = get_weather_summary()
    print(result)
# Output: Time: 2025-12-21 18:04, Temperature: 29.1°C, Condition: Patchy light rain with thunder
