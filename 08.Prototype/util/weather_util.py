import requests
import os
import urllib.request
from PIL import Image
import matplotlib.pyplot as plt


def get_weather(static_path, lat, lng):
    filename = f'{static_path}/keys/OpenWeatherApiKey.txt'
    with open(filename) as file:
        weather_key = file.read()

    base_url = 'https://api.openweathermap.org/data/2.5/onecall'
    url = f'{base_url}?lat={lat}&lon={lng}&appid={weather_key}&units=metric&lang=kr'
    result = requests.get(url).json()

    desc = result['current']['weather'][0]['description']
    temp = result['current']['temp']
    icon_code = result['current']['weather'][0]['icon']
    icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png'

    html = f'''<img src="{icon_url}" height="32"><strong>{desc}</strong>,
        온도: <strong>{temp:.1f}</strong>&#8451'''

    return html
