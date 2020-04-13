#to use pythons built-in functions, I have to import them e.g for random:
# import random, sys
# random.randint(1,10) # returns a random integer from 1 to 10
import sys
print('Hello')
sys.exit()
print('goodbye')

#I can import modules and get access to new functions
#The modules that come with Python are called the standard librayr,
# but I can also instal 3rd party modules using the pip tool

#sys.exit() immedialtely quits my program
#the pyperclip third party module has copy() and paste() functions for reading and writing text to the clipboard

 

#using the pip program to install pyperclip. this is a module that lets me copy and paste text to and form the clipboard
#on my cmd line, go to : C:\Users\Dan\AppData\Local\Programs\Python\Python38-32\Scripts
#then in cmdline do: pip.exe install pyperclip
#now I can import pyperclip

#pyperclip has a copy and paste function for copying and pasting text
#pyperclip.copy('blah')
#pyperclip.paste()   #shows blah
