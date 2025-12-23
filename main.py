from dotenv import load_dotenv

load_dotenv()

def get_weather_summary(temperature, condition):
    """Return a weather summary string."""
    return f"Temperature: {temperature}°C, Condition: {condition}"

if __name__ == "__main__":
    result = get_weather_summary(22, "Sunny")
    print(result)
# Output: Temperature: 22°C, Condition: Sunny
