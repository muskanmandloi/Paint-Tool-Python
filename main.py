import requests 
def complete_api_link(zip_code, api_key):
  complete_api_link = "http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}".format(zip_code,api_key)
  print(complete_api_link)
  complete_api_link("560011","5fd536d5f7f2227c84fe6d944b3b5b01")