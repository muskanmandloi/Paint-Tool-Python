import requests 
import os
from datetime import datetime

location = input("Enter the city name: ")
def complete_api_link(zip_code, api_key):
   complete_api_link = "http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}".format(zip_code,api_key)
   print(complete_api_link)
complete_api_link("560011","5fd536d5f7f2227c84fe6d944b3b5b01")
api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data)

if api_data['cod'] == '404':
    print("Invalid City : {}, Please check city name again".format(location))
else:
    temp_city = ((api_data['main']['temp']) -273.15)
    weather_desc = api_data['wheather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("*********************************")
    print("weather state for - {} || {}".format(location.upper(),date_time))
    print("*********************************")

    print("Current temprature is : {:.2f} deg C".format(temp_city))
    print("current weather desc :",weather_desc)
    print("current Humidity :",hmdt)
    print("current wind speed :",wind_spd,'kmph')