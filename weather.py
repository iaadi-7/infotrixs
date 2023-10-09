import requests
import json
import time
from datetime import datetime

API_KEY = "6bbfa25ff5e7cbfd099f824af587864c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
def get_weather(city_name):
    params = {'q' : city_name, 'appid' : API_KEY, 'units' : 'metric'}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print("Error : Unable to fetch weather data.")
        return None
    
def main():
    while True:
        print("----------------------------------------")
        print("🌙 Weather Checking App ⛅")
        print("----------------------------------------")
        print("Select your choice... ")
        print("1.   Check Weather by city name")
        print("2.   Add city to favourites")
        print("3.   Exit")
        print("----------------------------------------")

        choice = input("Enter your choice : ")
        if choice == "1":
            city_name = input("Enter your city name : ")
            weather_data = get_weather(city_name)
            if weather_data:
                temp_city = weather_data['main']['temp']
                weather_desc = weather_data['weather'][0]['description']
                hmdt = weather_data['main']['humidity']
                wind_speed = weather_data['wind']['speed']
                date_time = datetime.now().strftime("%d %b %Y || %I:%M:%S %p")
                print("-------------------------------------------------------------------")
                print("🌙 ⛅ Weather Stats for - {} || {}".format(city_name.upper(), date_time))
                print("-------------------------------------------------------------------")
                print("Current Temperature   : {:.2f} deg C" .format(temp_city))
                print("Current weather desc  :", weather_desc)
                print("Current humidity      :", hmdt, "%")
                print("Current wind speed    :", wind_speed, 'kmph')
                print("-------------------------------------------------------------------")
        elif choice == "2":
            pass
        elif choice == "3":
            print("Thank You...❤️")
            print("See you soon...")
            break
        else:
            print("Invalid Choice. Try again")
        time.sleep(15 + 15 * (hash(city_name) % 4))
if __name__ == "__main__":
    main()
