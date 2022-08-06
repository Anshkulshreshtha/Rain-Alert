import requests
from twilio.rest import Client
import os

owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "2a7f1fbe490a09f8765d1f427f37dd55"
account_sid = "AC03cad590afc9096d1f164e3d1864de0f"
auth_token = "80755aea82a996baa832dbd2b0eb07e8"

# Location is set to delhi , if you have to change it then select your own lat, lon

weather_params = {
    "lat": 28.6667,
    "lon": 77.2167,
    "appid": api_key,
    "except": "current,minutely,daily"
}

response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+19089488551',
        body="It's going to rain today,please bring umbrella with you",
        to='+91 87558 84597'
    )
    print(message.sid)
