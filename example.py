import json

with open('weather.json') as f:
    d = json.load(f)
    # print(d)

tmp = d['current']['temp_c']
cnd = d['current']['condition']['text']

def get_weather_summary(temperature, condition):
    """Return a weather summary string."""
    return f"Temperature: {temperature}°C, Condition: {condition}"

if __name__ == "__main__":
    result = get_weather_summary(tmp, cnd)
    print(result)
