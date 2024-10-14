import requests

# Function to get coordinates (latitude, longitude) from city name
def get_coordinates(city):
    geo_url = f"https://geocode.xyz/{city}?json=1"
    response = requests.get(geo_url)
    if response.status_code == 200:
        data = response.json()
        return data.get("latt"), data.get("longt")
    else:
        print("Error fetching coordinates.")
        return None

# Function to get weather data from Open-Meteo API
def get_weather(lat, lon):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(weather_url)
    if response.status_code == 200:
        weather_data = response.json()["current_weather"]
        temperature = weather_data["temperature"]
        windspeed = weather_data["windspeed"]
        return temperature, windspeed
    else:
        print("Error fetching weather data.")
        return None

# Main program
def weather_app():
    print("Welcome to the Weather Forecast App by Samuel Adenekan")
    while True:
        city = input("Enter a city name (or type 'Exit' to quit): ")
        if city.lower() == 'exit':
            break
        coordinates = get_coordinates(city)
        if coordinates:
            lat, lon = coordinates
            weather = get_weather(lat, lon)
            if weather:
                temperature, windspeed = weather
                print(f"Temperature: {temperature}°C, Windspeed: {windspeed} km/h")
        else:
            print("Could not retrieve weather information. Please try again.")

# Run the app
if __name__ == "__main__":
    weather_app()
