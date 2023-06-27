import requests

def get_5_day_forecast(city):
    api_key = '506273999320445ca59239b93871dc02'
    base_url = 'http://api.openweathermap.org/data/2.5/forecast'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    forecast_data = response.json()

    return forecast_data
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    city = 'London'  # Example city, you can get it from user input
    forecast_data = get_5_day_forecast(city)

    return render_template('weather.html', forecast_data=forecast_data)
