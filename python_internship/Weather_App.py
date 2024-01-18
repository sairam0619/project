import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            display_weather(data)
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

def display_weather(data):
    city = data["name"]
    country = data["sys"]["country"]
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print(f"Weather in {city}, {country}:")
    print(f"Description: {description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")

def main():
    api_key = "bd5e378503939ddaee76f12ad7a97608"  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")

    get_weather(api_key, city)

if __name__ == "__main__":
    main()
