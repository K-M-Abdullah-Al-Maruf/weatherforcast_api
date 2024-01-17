import json
import requests

url = "http://api.weatherapi.com/v1/forecast.json"
api_key = "5e619981755b4c10a41180919241601"

parameter = {
    "key": api_key,
    "q" : "Bangladesh"
}

response = requests.get(url, params=parameter)

print("Is the response a json file? =", "application/json" in response.headers["Content-Type"], end="\n\n")

data = response.json()
print(data)
# data_param = {
#     'country': data.get('location').get('country'),
#     'name': data.get('location').get('name'),
#     'date': data.get('location').get('localtime').split(' ')[0],
#     'time': data.get('location').get('localtime').split(' ')[1],
#     'temp_c': data.get('current').get('temp_c'),
#     'temp_f': data.get('current').get('temp_c')
# }
#
# new_data = json.dumps(data_param)
#
# print("Country =", data_param['country'])
# print("City =", data_param['name'])
# print("Date =", data_param['date'])
# print("Time =", data_param['time'])
# print("Temp =", data_param['temp_c'],"C")
# print("Temp =", data_param['temp_f'],"F")

