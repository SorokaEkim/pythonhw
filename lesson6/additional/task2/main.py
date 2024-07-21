import requests


API_KEY = '61d60acb3d6ab95dab584065fb49be3b'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
CITY = 'Cheboksary'
CELVIN_CONST = 273.15

url = BASE_URL + 'appid=' + API_KEY + '&q=' + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_kelvin_feels_like = response['main']['feels_like']
speed_wind = response['wind']['speed']
humidity = response['main']['humidity']

def celvin_to_celsius(temp_kelvin):
    return round(temp_kelvin - CELVIN_CONST, 2) 

city_temp = celvin_to_celsius(temp_kelvin)
city_temp_feels_like = celvin_to_celsius(temp_kelvin_feels_like)


print(f'Город: {CITY}\nТемпература вохдуха: {city_temp}\nТемпература вохдуха по ощущениям: {city_temp_feels_like}\nСкорость ветра: {speed_wind} м/c\nОтносительная влажность: {humidity}')
