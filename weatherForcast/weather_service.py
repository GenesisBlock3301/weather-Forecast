import requests
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def get_weather(city_name:str):
    api_key = '0d10c44bb9633604f35d97028b66c3fb'
    response = requests.get(url.format(city_name,api_key))
    data = response.json()
    return {
        'city': data.get('name'),
        'weather': data['weather'][0]['main'],
        'icon': data['weather'][0]['icon'],
        'temp':data['main']['temp'] - 273
    }