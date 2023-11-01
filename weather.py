import requests

places = {
    'london': {
        'latitude': 51.5085,
        'longitude': -0.1257
    },
    'lichfield': {
        'latitude': 52.6873,
        'longitude': -1.8057
    }
}

weather_api_url = "https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FLondon"

def fetch_weekly_weather_data():
    response = requests.get(weather_api_url)
    
    data = response.json()
    
    if response.status_code == 200:
        weekly_temperatures = data['daily']['temperature_2m_max']
        unit = data['daily_units']['temperature_2m_max']
        return weekly_temperatures
    else:
        print("Failed to fetch weather data. Status code:", response.status_code)
        return None

def calculate_average_temperature(weekly_temperatures):
    total_temperature = 0
    count = 0
    for day in weekly_temperatures:
        temperature = day
        total_temperature += temperature
        count += 1

    average_temperature = total_temperature / count
    return average_temperature

weekly_temperatures = fetch_weekly_weather_data()
average_temp = calculate_average_temperature(weekly_temperatures)

if average_temp is not None:
    print("The average temperature for the week is:", average_temp, "°C")
else:
    print("Unable to calculate the average temperature.")
