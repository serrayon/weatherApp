import requests 
import config


BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
city = input("Enter a city name: ")

# URL we are trying to hit found on the documentation page of weather api
request_url = f"{BASE_URL}?appid={config.API_KEY}&q={city}&units=imperial"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #print(data)
    weather = data['weather'][0]['description']
    #print(weather)
    temperature = round(data['main']['temp'], 2)
    #print(temperature)
    print("Weather:" , weather)
    print("Temperature:", temperature, "fahrenheit")


else:
    print("An error occured.")
