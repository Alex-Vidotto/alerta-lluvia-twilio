import os
import requests
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_TOKEN')
APP_KEY = os.environ.get('OWM_KEY')

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters ={
    "lat":-2.52972,
    "lon": -44.30278,
    "appid":APP_KEY,
    "cnt":4,
}

data = requests.get(url=OWM_Endpoint, params=parameters)
data.raise_for_status()
data_dict = data.json()

will_rain = False

data_weather = [i["weather"][0]["id"] for i in data_dict["list"]]
for i in data_weather:
    if i < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Va a llover\nLleva paraguas",
        from_="+14173842275",
        to="+54 numero de destino",
    )
    print(message.status)
