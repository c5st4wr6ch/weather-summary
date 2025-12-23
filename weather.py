import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city="Jakarta"):
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": os.getenv("WEATHER_API_KEY"),
        "q": city,
    }
    url2="https://api.weatherapi.com/v1/current.json?key=" + os.getenv("WEATHER_API_KEY") + "&q=" + city
    print(url2)
    # data = requests.get(url, params=params, timeout=10).json()
    data = requests.get(url2).json()
    print(data)
    # day = data["forecast"]["forecastday"][0]["day"]

    # res_weather = {
    #     "city": data["location"]["name"],
    #     "temp_avg": day["avgtemp_c"],
    #     "temp_max": day["maxtemp_c"],
    #     "temp_min": day["mintemp_c"],
    #     "rain_chance": day["daily_chance_of_rain"],
    #     "condition": day["condition"]["text"]
    # }
    # return res_weather

if __name__ == "__main__":
    result = get_weather("Jakarta")
    print(result)