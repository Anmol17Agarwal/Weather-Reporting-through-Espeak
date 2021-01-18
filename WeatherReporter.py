#http://api.openweathermap.org/data/2.5/weather?appid=08ac83007672faa2822e5f9ae0e7ad82&q=allahabad (copy url and check json response)
import requests, json
import subprocess

api_key = "08ac83007672faa2822e5f9ae0e7ad82" #add api key please prefer your own api key
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ") 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 


response = requests.get(complete_url)

x = response.json() 

if x["cod"] != "404": 

    y = x["main"]
    Temp = y["temp"]
    Pressure = y["pressure"]
    Humid = y["humidity"]
    z = x["weather"]
    description = z[0]["description"]
    print(description)
    print("Temperature(K) = {0} | Atmospheric pressure(hPa) = {1} | Humidity (%) = {2}".format(Temp,Pressure,Humid))
    data = "City name is "+str(city_name)+"Weather is "+str(description)+"now"+" "+"Temperature"+str(Temp)+" "+"Pressure"+str(Pressure)+" "+"Humidity"+str(Humid)
    subprocess.call(["sudo","espeak",data])
    
else: 
    print(" City Not Found ") 
    data="Sorry, city Not Found"
    subprocess.call(["sudo","espeak",data])
