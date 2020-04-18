import requests

HOURLY_RED_HAT = "https://api.weather.gov/gridpoints/RAH/73,57/forecast/hourly"


def get_temperature():
    result = requests.get(HOURLY_RED_HAT)
    return result.json()["properties"]["periods"][0]["shortForecast"]


print(get_temperature())
