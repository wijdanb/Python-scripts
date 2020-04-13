import webbrowser
#webbrowser modules open() function can launch a new browser to a specified url
#webbrowser.open('https://google.com') #opens google.com, returns True
#webbrowser module can only do .open()

#I can write a simple script that automatically launches the browser to a specific address on google maps
# look at mapit.py file in my PythonScripts folder

#then in cmd run I type: mapit 6844 golden hillsway
# or if I have the address copied on a clipboard just type: mapit



#downloading files from the web with requests module
# request module lets me easily download files from the web without having to worry about complicated issues such as network errors, connection problems and data compression
# request module is 3rd part so I have to use pip to install it
# To install on windows its:
    #win+r to open "Run Dialog"
    # type cmd then press enter
    # change dir to C:\Users\Dan\AppData\Local\Programs\Python\Python38-32\Scripts"
    # then run: pip install requests

import requests
#to download a file, call requests.get()   this function returns a response object which ill store in a variable called res
res = requests.get('https://www.gutenberg.org/files/84/84-0.txt') #this is Frankenstein the book in txt

#this response object contains the response that the webserver gave me for this request
#I can tell if the request for the web page succeeded by checking the status code attribute of the response object
res.status_code #200    #200 means everythinfs OK           404 means error
#so if the request succeeded, the downloaded web page is stored as a string in the response objects text variable
#.text holds a large string of the entire file
len(res.text)
print(res.text[:500]) #prints the first 500 characters

#a better way to check for success is to call the raise_for_status() method
#this method will raise an exception if there was an error downloading the file and do nothing if the download succeeded
res.raise_for_status()
#badRes = request.get('http://dahnb sdshajbdhasbdyhsabdyhbadas.com/dasdbahbdahybda')
#badRes.raise_for_status() #this will stop the program which is good. If I want to circumvent the stopping of the program, I can put this in a try except block

#So now I can save the web page to a file on my hard drive with the standard open() function BUT there are some differences
# 1st difference is, I must open the file in Write-binary mode by passing the string 'wb' as 2nd argument to open()
#even if the page is in plain text, I still need to write-binary data instead of text data in order to maintain the Unicode encoding of the text
playFile = open('Frankenstein.txt', 'wb')

#these steps work for any type of file I download from the web using requests

#to write the webpage file to a file on my hard drive, I need a for loop with the response objects iter_content() 
#iter_content() method returns chunks of the content on each iteration through the loop
    #each chunk is of the data type: byte
    # I get to specify how many bytes each chunk will contain
for chunk in res.iter_content(100000): #passing 100000 bytes per iteration through this loop
    playFile.write(chunk)
playFile.close()

#for more on requests:   https://requests.readthedocs.io/en/master/
# request module is good for downloading files or web pages when I have the exact url to download
#BUT if I have to log into a website first or figuring out the url is a complicated process, then using a request might not be the best way to do it.
#Selenium might be better which lets my Python scripts control the web browser directly
 

# Web scraping:   How to write programs that pull info from web pages
#Parsing HTML with Beautiful Soup module:
#request module handles downloading the web page itself but it gets me a huge string of text of the pages HTML
#In order to locate the text I need inside this huge string, I need to parse the HTML and to do this, I use Beautiful soup module
#Beautiful soup is a 3rd party module
#To install Beautiful soup:
 # To install on windows its:
    #win+r to open "Run Dialog"
    # type cmd then press enter
    # change dir to C:\Users\Dan\AppData\Local\Programs\Python\Python38-32\Scripts"
    # then run: pip install beautfiulsoup4
import bs4
import requests

#I'll web scrape the price information off of amazon page. Amazon are assholes about web scraping so im using: https://camelcamelcamel.com/ to get amazon prices for stuff and scraping that website

#This soup object is now ready to find html elements in the web page I downloaded
 
#I pass select() a string of the CSS selector for the element or elements that I want to look at
# to find CSS selector for price, I right click on price and inspect element and see the class name. Then on the elements tab, I highlight the div or span and right click and press Copy Selector path
#soup.select('#priceblock_ourprice') #.select returns a list of all these element objects for all the matching elements

import bs4 
import requests

def getAmazonPrice(productUrl):
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(productUrl,headers=headers)
    print(res.status_code)
    priceText = res.text
    soup = bs4.BeautifulSoup(priceText,'html.parser')
    #main way soup object finds html elements is by the select() method
    #I pass select() a string of the CSS selector for the element or elements that I want to look at
    # to find CSS selector for price, I right click on price and inspect element and see the class name. Then on the elements tab, I highlight the div or span and right click and press Copy Selector path
    soup.select('span.green')
    for price in soup.select('span.green'):
        print('Price is: ' + price.string)

getAmazonPrice('https://camelcamelcamel.com/Automate-Boring-Stuff-Python-Programming/product/1593275994')
 


# Controlling the browser with the Selenium module
#Selenium module will launch a Web Browser that I can programmatically control from my Python program
#I can call functions that will find HTML in the browser or fill out forms and login fields and click submit buttons
#because it launches a web browser, its a bit slower and hard to run in the background if for example I need to download some files from the web
#Selenium is a third party module
#To install Selenium:
 # To install on windows its:
    #win+r to open "Run Dialog"
    # type cmd then press enter
    # change dir to C:\Users\Dan\AppData\Local\Programs\Python\Python38-32\Scripts"
    # then run: pip install selenium

#Ill be using firefox web browser. Selenium will control firefox browser
# to import selenium, its a bit different
from selenium import webdriver
#to launch firefox browser with selenium i use webdriver.firefox
browser = webdriver.Firefox() #launches the firefox window. Now I can control this by calling methods on this browser object
# most basic is get() method which sends this browser to a url
browser.get('https://www.google.com') #python code controls the browser. Eveyrhting that a web browser does, selenium is simulating
#If I want to click on something, I right-click what I want to click on and inspect element then right click and select CSS Selecotr
elem = browser.find_element_by_css_selector('.gLFyf')
#.click() simulates clicking on that link
elem.click() #will click on searchbar on google.com

# Instead of specifying a unique CSS selector, I can specify a more general CSS selector that will match multiple elements
#using that, I can then call the find_elements_by_css_selector e.g if I wanted to get all paragraph elements:
#elems = browser.find_elements_by_css_selector('div')
#len(elems) #207
#So now I can click on pages but how do I type? I use sendkeys() and pass it any string that will be typed into the field
elem.send_keys('xcom2')
#selenium helps me by having a submit() method which does the same thing as pressing 'enter' on the search field
elem.submit()

#I can also control the browser itself using the browser objects' methods
#e.g if I want to press the back button on the browser I can call the back() function
browser.back()
#if I want to press the forward button on the browser, I can call forward()
browser.forward()
#if I want to press the refresh button on the browser, I can call refresh()
browser.refresh()
#if I want to close the browser I can call quit()
browser.quit()

#Now ill look at how my Python scripts can use selenium to read the content of the web pages
browser = webdriver.Firefox()
browser.get('https://reactjs.org/docs/getting-started.html')
elem = browser.find_element_by_css_selector('#gatsby-focus-wrapper > div > div > div > div.css-12vsfho > div > div > article > div > div.css-15weewl > p:nth-child(6)')
#all elements have a text member variable that contains a string of the text inside of that element
print(elem.text)
#if I want the entire text for the website, easiest thing I can do is just grab the 'html' or 'body' element which should contain the entire web page
elem = browser.find_element_by_css_selector('html')
print(elem.text)

                                            
#selenium has several different methods for getting web elements from the web page
#the ones ill use the most are:
    # browser.find_element_by_css_selector(selector)
    # browser.find_elements_by_css_selector(selector)
#but I can also:
    # browser.find_element_by_class_name(name)
    # browser.find_elements_by_class_name(name)
#also:
    #browser.find_element_by_id(id)
    #browser.find_elements_by_id(id)
#also by <a> element that completely match the text provided
    #browser.find_element_by_link_text(text)
    #browser.find_elements_by_link_text(text)
#also <a> elements that contain the text provided
    # browser.find_element_by_partial_link_text(text)
    # browser.find_elements_by_partial_link_text(text)
#also elements with a matching name attribute value
    # browser.find_element_by_name(name)
    # browser.find_elements_by_name(name)
#also elements with a matching tag name(case insensitive; an <a> element is matched by 'a' and 'A')
    # browser.find_element_by_tag_name(name)
    # browser.find_elements_by_tag_name(name)

#TO learn more about selenium: https://selenium-python.readthedocs.io/


