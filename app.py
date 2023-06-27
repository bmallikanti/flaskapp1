from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

def get_current_weather(city):
    api_key = '627f2ace53615d9038aa79e9907b9450'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

def get_5_day_forecast(city):
    api_key = '627f2ace53615d9038aa79e9907b9450'
    base_url = 'http://api.openweathermap.org/data/2.5/forecast'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def get_weather_icon_url(icon_code):
    base_url = 'http://openweathermap.org/img/wn/'
    icon_url = f'{base_url}{icon_code}@2x.png'
    return icon_url

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    current_weather_data = get_current_weather(city)
    if 'weather' in current_weather_data:
        icon_code = current_weather_data['weather'][0]['icon']
        icon_url = get_weather_icon_url(icon_code)
        return render_template('weather.html', city=city, current_weather_data=current_weather_data, icon_url=icon_url)
    else:
        return render_template('no_forecast.html', city=city)

@app.route('/forecast', methods=['POST', 'GET'])
def forecast():
    if request.method == 'POST':
        city = request.form['city']
        forecast_data = get_5_day_forecast(city)
        if forecast_data.get('cod') == '200':
            return render_template('forecast.html', city=city, forecast_data=forecast_data)
        else:
            return render_template('no_forecast.html', city=city)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()
