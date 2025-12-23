import requests
import os

def get_weather(city="Jakarta"):
    url = "https://api.weatherapi.com/v1/forecast.json"
    params = {
        # "key": os.getenv("WEATHER_API_KEY"),
        # "q": city,
        # "days": 1,
        # "aqi": "no",
        # "alerts": "yes"
    }
    data = requests.get(url, params=params, timeout=10).json()
    print(data)
    day = data["forecast"]["forecastday"][0]["day"]

    res_weather = {
        "city": data["location"]["name"],
        "temp_avg": day["avgtemp_c"],
        "temp_max": day["maxtemp_c"],
        "temp_min": day["mintemp_c"],
        "rain_chance": day["daily_chance_of_rain"],
        "condition": day["condition"]["text"]
    }
    return res_weather

if __name__ == "__main__":
    result = get_weather("Jakarta")
    print(result)