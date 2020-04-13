#Fetching current weather data
'''
Checking the weather seems fairly trivial: Open your web browser, click the address bar, type the URL to a weather website (or search for one and then click the link), wait for the page to load, look past all the ads, and so on.

Actually, there are a lot of boring steps you could skip if you had a program that downloaded the weather forecast for the next few days and printed it as plaintext. This program uses the requests module from Chapter 12 to download data from the web.

Overall, the program does the following:

Reads the requested location from the command line
Downloads JSON weather data from OpenWeatherMap.org
Converts the string of JSON data to a Python data structure
Prints the weather for today and the next two days

So the code will need to do the following:

Join strings in sys.argv to get the location.
Call requests.get() to download the weather data.
Call json.loads() to convert the JSON data to a Python data structure.
Print the weather forecast.

got an API key(also called app ID) from : https://openweathermap.org/api/
Step 1: Get location from cmdline argument
'''

#! python3
# getOpenWeather.py -prints the weather for a location from the cmd line

#In Python, command line arguments are stored in the sys.argv list. The APPID variable should be set to the API key for your account. Without this key, your requests to the weather service will fail. After the #! shebang line and import statements, the program will check that there is more than one command line argument. (Recall that sys.argv will always have at least one element, sys.argv[0], which contains the Python script’s filename.) If there is only one element in the list, then the user didn’t provide a location on the command line, and a “usage” message will be provided to the user before the program ends.
APPID = 'd0c703cbe72ae420eff61426ad9a8ac2'
import json, requests, sys    # sys.argv hold ['getOpenWeather.py', 'San', 'Francisco,', 'US'

#Compute location from cmd line args
if len(sys.argv) < 2:
#The OpenWeatherMap service requires that the query be formatted as the city name, a comma, and a two-letter country code (like “US” for the United States). You can find a list of these codes at https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2. Our script displays the weather for the first city listed in the retrieved JSON text. Unfortunately, cities that share a name, like Portland, Oregon, and Portland, Maine, will both be included, though the JSON text will include longitude and latitude information to differentiate between the cities.Command line arguments are split on spaces. The command line argument San Francisco, US would make sys.argv hold ['getOpenWeather.py', 'San', 'Francisco,', 'US']. Therefore, call the join() method to join all the strings except for the first in sys.argv. Store this joined string in a variable named location.
    print('Usage: getOpenWeather.py city_name, 2-letter_countr_code')
    sys.exit()
location = ''.join(sys.argv[1:])

#TODO downlaod JSON data from OpenWeatherMap.orgs API

#OpenWeatherMap.org provides real-time weather information in JSON format. First you must sign up for a free API key on the site. (This key is used to limit how frequently you make requests on their server, to keep their bandwidth costs down.) Your program simply has to download the page at https://api.openweathermap.org/data/2.5/forecast/daily?q=<Location>&cnt=3&APPID=<APIkey>, where <Location> is the name of the city whose weather you want and <API key> is your personal API key. Add the following to getOpenWeather.py.
# Download the JSON data from OpenWeatherMap.org's API.
#We have location from our command line arguments. To make the URL we want to access, we use the %s placeholder and insert whatever string is stored in location into that spot in the URL string. 
url ='https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location,APPID)  
#We store the result in url and pass url to requests.get(). The requests.get() call returns a Response object,
response = requests.get(url)
print(response)
#which you can check for errors by calling raise_for_status(). If no exception is raised, the downloaded text will be in response.text.
response.raise_for_status()

#uncomment to see the rawJSON text:
#print(response.text)

#The response.text member variable holds a large string of JSON-formatted data. To convert this to a Python value, call the json.loads() function. 



#TODO: Load JSON data into a python variable
weatherData = json.loads(response.text)
print(weatherData['weather'][0]['main'])
#print weather descriptions
#Notice how the code stores weatherData['list'] in the variable w to save you some typing
print('Current weather in %s:' %(location))
#ou use w[0], w[1], and w[2] to retrieve the dictionaries for today, tomorrow, and the day after tomorrow’s weather, respectively. Each of these dictionaries has a 'weather' key, which contains a list value. You’re interested in the first list item, a nested dictionary with several more keys, at index 0. Here, we print the values stored in the 'main' and 'description' keys, separated by a hyphen.
print(weatherData['weather'][0]['main'],'-',weatherData['weather'][0]['description'])
print()
#convert f to c
temp = weatherData['main']['temp']
celsiusTemp = temp - 273
print('Current temp is:' + str(celsiusTemp))
tempFeels= weatherData['main']['feels_like']
tempFeels = tempFeels-273
print('FEELS LIKE: ' + str( tempFeels ))


#print(weatherData['main']['temp'],'-',weatherData['main']['feels_like']) 
