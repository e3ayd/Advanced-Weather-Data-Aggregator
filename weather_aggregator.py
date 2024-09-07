# weather_aggregator.py

import requests
from config import OPENWEATHERMAP_API_KEY, WEATHERBIT_API_KEY, DEFAULT_CITY

def fetch_openweathermap_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def fetch_weatherbit_data(city):
    url = f"https://api.weatherbit.io/v2.0/current?city={city}&key={WEATHERBIT_API_KEY}&units=M"
    response = requests.get(url)
    return response.json()

def aggregate_weather_data(city):
    data_openweathermap = fetch_openweathermap_data(city)
    data_weatherbit = fetch_weatherbit_data(city)

    # Aggregating data from both sources
    aggregated_data = {
        "city": city,
        "temperature": (data_openweathermap['main']['temp'] + data_weatherbit['data'][0]['temp']) / 2,
        "humidity": (data_openweathermap['main']['humidity'] + data_weatherbit['data'][0]['rh']) / 2,
        "description_openweathermap": data_openweathermap['weather'][0]['description'],
        "description_weatherbit": data_weatherbit['data'][0]['weather']['description']
    }

    return aggregated_data

def display_weather_report(data):
    print(f"Weather report for {data['city']}:")
    print(f"Temperature: {data['temperature']}°C")
    print(f"Humidity: {data['humidity']}%")
    print(f"OpenWeatherMap description: {data['description_openweathermap']}")
    print(f"Weatherbit description: {data['description_weatherbit']}")

if __name__ == "__main__":
    city = input("Enter city name (default is London): ") or DEFAULT_CITY
    aggregated_data = aggregate_weather_data(city)
    display_weather_report(aggregated_data)
