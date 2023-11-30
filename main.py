import requests
import os
from twilio.rest import Client

API_KEY = "b1eff94c1b91a8120b5cfc08e57827dd"
MY_LAT = 53.800755
MY_LON = -1.549077
account_sid = "ACf274c6011a90a9e4f2349f5aad53beea"
auth_token = "bbf56600bff40ae88f0eaac5f2b208aa"


parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4,
}

#api_link = f"api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
api_link = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(api_link, params=parameters)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_='+447723425802',
        to='+447586471746'
    )

    print(message.status)