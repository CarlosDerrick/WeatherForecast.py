import requests

class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        url = f"https://api.weather.com/v1/forecast?city={city}&apiKey={self.api_key}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            if "current" in data:
                temperature = data["current"]["temperature"]
                description = data["current"]["description"]

                print(f"Weather Forecast for {city}:")
                print(f"- Temperature: {temperature}°C")
                print(f"- Description: {description}")
            else:
                print(f"No weather forecast found for {city}.")
        else:
            print("Unable to retrieve weather forecast.")

def main():
    api_key = "YOUR_API_KEY"
    city = "New York"

    forecast = WeatherForecast(api_key)
    forecast.get_weather(city)

if __name__ == "__main__":
    main()
