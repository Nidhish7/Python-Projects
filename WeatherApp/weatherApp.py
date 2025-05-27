import requests

# Define API keys and base URL for OpenWeatherMap API

api_key = "2d1b21e2ce92ca33027dc5f6f2d69249"
base_URL = "http://api.openweathermap.org/data/2.5/weather?"


# Function to get the weather data

def getWeather(city):
    # Construct the URL to get the weather data for the specified city
    url = f"{base_URL}q={city}&appid={api_key}&units=metric"

    # Send a GET request to API
    response = requests.get(url)

    # Check if the request to the API
    if response.status_code == 200:
        data = response.json()

        # Extract weather information from the response

        main = data["main"]
        weather = data["weather"][0]
        # Return data as dictionary
        return {
            "city": city,
            "temperature": main["temp"],
            "humidity": main["humidity"],
            "description": weather["description"]
        }
    else:
        return None
'''
        # Display weather details
        print(f"Weather in {city}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather["description"]}")

    else:
        print(f"City {city} not found.")
'''



# Main function to run the app
if __name__ == "__main__":
    city = input("Enter the city name: ")
    weather = getWeather(city)
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Weather: {weather['description']}")
    else:
        print(f"City {city} not found.")