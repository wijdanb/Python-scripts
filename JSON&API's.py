#JSON
#JavaScript Object Notation is a popular way to format data as a single human-readable string. JSON is the native way that JavaScript programs write their data structures and usually resembles what Python’s pprint() function would produce. You don’t need to know JavaScript in order to work with JSON-formatted data.
'''
Here’s an example of data formatted as JSON:

{"name": "Zophie", "isCat": true,
 "miceCaught": 0, "napsTaken": 37.5,
 "felineIQ": null}
'''
#JSON is useful to know, because many websites offer JSON content as a way for programs to interact with the website. This is known as providing an application programming interface (API). Accessing an API is the same as accessing any other web page via a URL. The difference is that the data returned by an API is formatted (with JSON, for example) for machines; APIs aren’t easy for people to read.
#Many websites make their data available in JSON format. Facebook, Twitter, Yahoo, Google, Tumblr, Wikipedia, Flickr, Data.gov, Reddit, IMDb, Rotten Tomatoes, LinkedIn, and many other popular sites offer APIs for programs to use. Some of these sites require registration, which is almost always free. You’ll have to find documentation for what URLs your program needs to request in order to get the data you want, as well as the general format of the JSON data structures that are returned. This documentation should be provided by whatever site is offering the API; if they have a “Developers” page, look for the documentation there.

'''
Using APIs, you could write programs that do the following:

Scrape raw data from websites. (Accessing APIs is often more convenient than downloading web pages and parsing HTML with Beautiful Soup.)
Automatically download new posts from one of your social network accounts and post them to another account. For example, you could take your Tumblr posts and post them to Facebook.
Create a “movie encyclopedia” for your personal movie collection by pulling data from IMDb, Rotten Tomatoes, and Wikipedia and putting it into a single text file on your computer.
You can see some examples of JSON APIs in the resources at https://nostarch.com/automatestuff2/.
'''

#JSON isn’t the only way to format data into a human-readable string. There are many others, including XML (eXtensible Markup Language), TOML (Tom’s Obvious, Minimal Language), YML (Yet another Markup Language), INI (Initialization), or even the outdated ASN.1 (Abstract Syntax Notation One) formats, all of which provide a structure for representing data as human-readable text. This book won’t cover these, because JSON has quickly become the most widely used alternate format, but there are third-party Python modules that readily handle them.

#JSON MODULE

#Python’s json module handles all the details of translating between a string with JSON data
#and Python values for the json.loads() and json.dumps() functions.

#JSON can’t store every kind of Python value. It can contain values of only the following data types:
    #strings, integers, floats, Booleans, lists, dictionaries, and NoneType

#JSON cannot represent Python-specific objects, such as:
#   File objects, CSV reader or writer objects, Regex objects, or Selenium WebElement objects.

#Reading JSON with the loads() Function
#To translate a string containing JSON data into a Python value, pass it to the json.loads() function. (The name means “load string,” not “loads.”) Enter the following into the interactive shell:
#After you import the json module, you can call loads() and pass it a string of JSON data.
#Note that JSON strings always use double quotes. It will return that data as a Python dictionary. Python dictionaries are not ordered, so the key-value pairs may appear in a different order when you print jsonDataAsPythonValue.
stringOfJsonData = '{"name" : "Dan", "isHuman" : true, "foodEaten" : 0, "humanIQ" : null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue  #{'name': 'Dan', 'isHuman': True, 'foodEaten': 0, 'humanIQ': None}

#Witing JSON with the dumps() function
#The json.dumps() function (which means “dump string,” not “dumps”) will translate a Python value into a string of JSON-formatted data. Enter the following into the interactive shell:
pythonValue =  {'name' : 'Dan', 'isHuman' : True, 'foodEaten' : 0, 'humanIQ' : None}  #The value can only be one of the following basic Python data types: dictionary, list, integer, float, string, Boolean, or None.
import json
newStringOfJsonData = json.dumps(pythonValue)
newStringOfJsonData  #'{"name": "Dan", "isHuman": true, "foodEaten": 0, "humanIQ": null}'

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
'''
#go to weather.py for this program







