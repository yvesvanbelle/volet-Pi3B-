import requests


def temp_humidity():
    WEATHER_DATA_URL  = 'http://api.openweathermap.org/data/2.5/weather?q=Koekelberg,BE&units=metric&APPID=375e74b400588fcf07d13dbd342093fc'

    weather_data = requests.get(WEATHER_DATA_URL)
    weather_data = weather_data.json()
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    return temp,humidity


if __name__ == '__main__':
    print(temp_humidity())