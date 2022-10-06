#Завдання 1
#урл http://api.open-notify.org/astros.json
#вивести список всіх астронавтів, що перебувають в даний момент на орбіті

import requests

url ='http://api.open-notify.org/astros.json'
response = requests.get(url)
response_json = response.json()
onorbit = response_json['people']

astronauts = [astronaut['name'] for astronaut in onorbit]
print("Astronauts on orbit now: ")
print(*astronauts, sep="\n")

#Завдання 2
#апі погоди (всі токени я для вас вже прописав)
#https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
#де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv)
#погода змінюється, як і місто. яке ви введете
#роздрукувати темпрературу та швидкість вітру. з вказівкою міста, яке було вибране


url2 ='https://api.openweathermap.org/data/2.5/weather?q=kyiv&appid=47503e85fabbabc93cff28c52398ae97&units=metric'
response = requests.get(url2)
all_data = response.json()

main = all_data["main"]
city = all_data["name"]
current_temperature = main["temp"]
wind_data = all_data["wind"]
wind_speed = wind_data["speed"]

print(" City = " + str(city), "\n Temperature = " + str(current_temperature), "\n Wind speed = " + str(wind_speed))
