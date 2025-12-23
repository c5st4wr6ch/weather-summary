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
    data = requests.get(url, params=params, timeout=10).json()

    res_weather = {
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "lat": data["location"]["lat"],
        "lon": data["location"]["lon"],
        "tz_id": data["location"]["tz_id"],
        "localtime_epoch": data["location"]["localtime_epoch"],
        "localtime": data["location"]["localtime"],

        "temp_c": data["current"]["temp_c"],
        "is_day": data["current"]["is_day"],
        "condition": {
            "text": data["current"]["condition"]["text"],
            "icon": data["current"]["condition"]["icon"],
            "code": data["current"]["condition"]["code"],
        },
        "wind_kph": data["current"]["wind_kph"],
        "pressure_mb": data["current"]["pressure_mb"],
        "precip_mm": data["current"]["precip_mm"],
        "humidity": data["current"]["humidity"],
        "cloud": data["current"]["cloud"],
        "feelslike_c": data["current"]["feelslike_c"],
        "windchill_c": data["current"]["windchill_c"],
        "heatindex_c": data["current"]["heatindex_c"],
        "dewpoint_c": data["current"]["dewpoint_c"],
        "vis_km": data["current"]["vis_km"],
        "gust_kph": data["current"]["gust_kph"],
        "short_rad": data["current"]["short_rad"],
        "diff_rad": data["current"]["diff_rad"],
        "dni": data["current"]["dni"],
        "gti": data["current"]["gti"],
    }

    return res_weather