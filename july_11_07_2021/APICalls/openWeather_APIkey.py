import requests
import json

apikey = "a85dc8ebdd75ac45d90d4ca5da40f612"
url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid='+apikey
print(url)
response = requests.get(url)
print(response)
print(json.dumps(response.json(),indent=4))