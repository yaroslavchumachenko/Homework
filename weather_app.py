import requests
import json
API_key = "96687c02763be4b168f17b73353e04a8"
city_url = "http://api.openweathermap.org/geo/1.0/direct"
base_url = "https://api.openweathermap.org/data/2.5/weather"
# def get_city(url, params):
#     r = requests.get(url, params=params)
#     data = r.json()
#     with open("city.json", "w") as f:
#         json.dump(data, f)
far_to_cel = lambda a: round((a-273.15), ndigits= 1)
far_to_cel(10)
    
while True:
    user_answ = input("Choose a city: ")

    r = requests.get(city_url, {"q" : user_answ, "appid" : API_key})
    data = r.json()
    try:
        data[0] == dict
        with open("city.json", "w") as f:
            json.dump(data, f)
        break
    except IndexError:
        print("We couldn't find your city, please try again...")

def get_weather(url):  
    with open("city.json", "r") as f:
        data = json.load(f)
    for list in data:
        for key, value in list.items():
            if key == "lat":
                lat = value
    for list in data:
        for key, value in list.items():
            if key == "lon":
                lon = value
               
    r = requests.get(url, {"lat" : lat, "lon" : lon, "appid" : API_key})
    data = r.json()
    
    for key, value in data.items():
        if key == "weather":
            for i in value:
                for a, b in i.items():
                    if a == "main":
                      print(f"The weather is {b}")  
        elif key == "main":
            for type, temp in value.items():
                if type == "temp":
                    print(f"Current temperature is {far_to_cel(temp)} of Celsius")
                elif type == "feels_like":
                    print(f"It feels like {far_to_cel(temp)} of Celsius")
                elif type == "temp_min":
                    print(f"Minimal temperature today is {far_to_cel(temp)} of Celsius")
                elif type == "temp_max":
                    print(f"And maximal temperature is {far_to_cel(temp)} of Celsius")

            
    with open("weather.json", "w") as f:
        json.dump(data, f)

# get_city(city_url, {"q" : "London", "appid" : API_key})
get_weather(base_url)


