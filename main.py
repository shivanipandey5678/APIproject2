import requests

API_KEY = "598e4cd49df2567d2aaf235c598c4039"
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q='
CITY_NAME = input("ENTER THE CITY NAME:")
URL = BASE_URL + CITY_NAME + "&appid=" + API_KEY
response = requests.get(URL)
data = response.json()
F = (data["main"]["temp"])
C = (F-273.15)
temp = str(round(C , 2))
print("Current temperature:" + temp + chr(176) + 'C')




