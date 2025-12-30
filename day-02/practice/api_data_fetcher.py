
import os
import requests

API_KEY='b313ba91fa0391261fc4b6cbb81027f8'
SERVER_URL='https://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data():
    output_file = os.path.join(os.path.dirname(__file__), "weather_output.txt")
    while True:
        city = input("-------------------------------------------\nEnter the city name or press q to quit: ")
        if city.lower() == 'q':
            print("Exiting the program.")
            break
        API_URL=f"{SERVER_URL}?q={city}&units=metric&appid={API_KEY}"
        response = requests.get(url=API_URL)
        if (response.status_code == 200):
            print("-------------------------------------------\nValid city name!\n-------------------------------------------")
            data = response.json()
            name = data['name']
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            wind = data['wind']['speed']
            country = data['sys']['country']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            print("-------------------------------------------")
            output = f"Weather in {name}, {country}: {temp}°C, {desc} with wind speed {wind} m/s. Feels like {feels_like}°C with humidity {humidity}%."
            print(output)
            print("-------------------------------------------")
            with open(output_file, "a", encoding="utf-8") as f:
                f.write(output + "\n")
        else:
            print("-------------------------------------------\nInvalid city name! Please check and try again.\n-------------------------------------------")
            print(response.status_code)
fetch_weather_data()