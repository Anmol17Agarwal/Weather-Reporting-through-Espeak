# Weather-Reporting-through-Espeak

## What is Weather Cloud?
Openweather NWP (numerical weather prediction) allows to calculate weather data for any location. We use proprietary convolutional neural network that collects and processes wide range of data sources to cover any location and consider the local nuances of climate. 

ML technology allows us to reach resolution about 500 m and very high accuracy between 90% and 100% with inaccuracy about 1%. Amongst data sources we feed to the NWP are 82,000 weather stations spread globally; national meteorological agencies (NOAA, Environment Canada, Met Office, etc.), radars, weather satellites.

- ### How to start and continue calling Openweather API in the best way
Openweather API is one of the most recognisable and elegant APIs. Powered by ML technologies, it provides all necessary for businesses weather information for any location on the globe. All you need to start using it is to sign up and call API straightforwardly.

- ### API key is all you need to call weather API
Please, use your API key in each API call. We do not process API requests without any API key. We count requests from all API keys that associate with your account.

## What is espeak?
eSpeakNG is a compact, open-source, software speech synthesizer for Linux, Windows, and other platforms. It uses a formant synthesis method, providing many languages in a small size. Much of the programming for eSpeakNG's language support is done using rule files with feedback from native speakers.

## How to get an API Key?
Create an account in OpenWeather,and choose current weather data.Click on pricing and opt for free API available.Now copy that API.

## Text to speech Configuration
Open the terminal on RaspberryPi and enable 3.5mm audio jack port
```
sudo raspi-config
```
![alt text](https://github.com/Anmol17Agarwal/Weather-Reporting-through-Espeak/blob/main/2021-01-18-164618_1920x1080_scrot.png)

- #### Configuration Window Opens

![alt text](https://github.com/Anmol17Agarwal/Weather-Reporting-through-Espeak/blob/main/2021-01-18-164623_1920x1080_scrot.png)

- Select System option

![alt text](https://github.com/Anmol17Agarwal/Weather-Reporting-through-Espeak/blob/main/2021-01-18-164630_1920x1080_scrot.png)

- Select Audio Option and enable audio jack

#### Install eSpeak Library
By running command
```
sudo apt-get install espeak
```

![alt text](https://github.com/Anmol17Agarwal/Weather-Reporting-through-Espeak/blob/main/2021-01-18-164823_1920x1080_scrot.png)
 #### Verify audio by entering command
 ```
 sudo espeak "Hey,Good Evening Master"
 ```
 connect rpi's audio jack with speaker or earphone for better standard.
 ![alt text](https://github.com/Anmol17Agarwal/Weather-Reporting-through-Espeak/blob/main/2021-01-18-164912_1920x1080_scrot.png)
 
 After running WeatherReporter.py code, it will asked to enter city name.After entering correct city name,you will listen name of city,condition of respective city,temperature,atmospheric pressure and humidity else on entering wrong city,you will listen `city not found` by BOT.
 
 ![alt text]()
