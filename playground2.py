import requests

url = ("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,"
       "wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

r = requests.get(url)
print(r.json())
data = r.json()
print(data['current_units']['time'])
print(data['current_units'])

url = "https://media.wired.com/photos/598e35fb99d76447c4eb1f28/master/pass/phonepicutres-TA.jpg"
r = requests.get(url)

with open('pics.png', mode='wb')as mf:
       mf.write(r.content)
