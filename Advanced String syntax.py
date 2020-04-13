# To use a single quote '  inside of a string is by doing:
    #using double quotes:
"That is Alice's cat"

#But if I need to use both single and double quotes inside a string, I need to use the escape char
# Escape characters lets me use characters that are otherwise impossible to put into a string
# Escape character is a backslash followed by which character I want to add to the string
# \ '   single quote
'That is Alice\'s cat'   #That is Alice's cat
# \"    double quote
"That is Alice's \"cat\" "  #That is Alice's "cat"
# \t    tab
# \n    newline (line break)
# \\    backslash

# If I have text that includes many backslashes that I dont want seen as the beggining escape character I can use a raw string
# In python, a raw string is the exact same as a normal string except it begins with a lowercase r right before. e.g:
#raw strings will literally print any backslashes in the string and ignore escape characters
r'Hey there'
r'That is Alice\'s cat'  #That is Alices\\s cat   because this is a raw string, the backslsahes are literally a part of the string

# To make a string multiline, I can use 3 single quotes or 3 double quotes and then I can tab anywhere in between those e.g:
print(""" BSAHDBNHANBAS
    inawdsnajndasnd
    dsdddddddddddddddddddddddddddd""")

# triple single/double quotes are super useful for big strings. Any backslash or quotes in the string are seen as being part as the string. Its super unlikely that there will be 3 double quotes in the string but if there is then I can use 3 single quotes


# Indexes, slices, in and not in operators work with strings
span = 'Hello world'
span[0] # gives me 'H'

span[1:5] #'ello
span[-1] # 'd'
'Hello' in span #True
'X' in span #False

#String methods
#Unlike list methods, String methods return a new string value since strings are immutable.
#upper() returns an uppercase version of the string but since strings are immutable, they cant be modified in place e.g:
blah = 'hi there'
blah.upper() #'HI THERE
blah    #'hi there
#to modify the variable I would have to instead do:
blah = blah.upper()
blah # HI THERE
#lower() does the opposite.
blah = blah.lower()
blah # hi there

#lower() and upper() are good for making comparisons

#strings also have a isupper() and islower() methods that returns a bool value depending on if the strings are uppercase or lowercase
span = 'Hello world'
span.islower() # False
span = 'HELLO'
span.isupper () # True
'12345'.islower() #False

#since the upper() and lower() string methods themselves return strings, I can call string methods on those retun string values as well
#expressions that do this will look like a chain of method calls e.g:
'hello'.upper().isupper() # True since im calling upper on'hello and then .upper returns 'HELLO' and so isupper returns true

#other string methods:
# isalpha() -letters only
# isalnum() - letters and number only
# isdecimal() - numbers only
# isspace() - whitespace only
# istitle() -titlecase only. Basically words that begin with Uppercase letter followed by only lowercase letters
# title() method that makes a string a title

# startswith() and endswith() methods return true if a string value that they're called on begins or ends respectively with the string thats passed to the method
'Hello World'.startswith('Hello') #True
'Hello World'.startswith('ello') #False
'Hello World'.endswith('World') #True
'Hello World'.endswith('w') #False

#join()method is useful when I have a list of strings that need to be joined together into a single string value
#join method is called on a string, gets passed a list of strings and returns a string
#common example is a string comma that I juse to join together a list of strings:
','.join(['cats','bats','rats']) # 'cats,bats,rats'
' '.join(['cats','bats','rats']) # 'cats bats rats'
''.join(['cats','bats','rats']) # 'catsbatsrats'

'\n\n'.join(['cats','bats','rats']) # 'cats   bats    rats'

#split() method does the opposite. Its called on a string value and returns a list of strings. Default is to split in white space characters
'My name is blah'.split() # ['My', 'name', 'is', 'blah']
#I can also split it on other characters by passing a different value e.g:
'My name is blah'.split('m') # ['My na', 'e is blah']

#ljust() and rjust() string methods will return a padded version of a string that they're called on with spaces inserted to left justify or right justify the tex
# 1st arg to both methods is the int length of the justified string
# optional 2nd arg can be passed to specify a different fill character(default is white space) other than a space
#python inserts as many empty spaces as possible to make the length 10
'Hello'.rjust(10) # '     Hello'
'Hello'.ljust(10) # 'Hello     '

'Hello'.rjust(10,'-') # '-----Hello'
'Hello'.ljust(10,'-') # 'Hello-----'

#center() that works like ljust and rjust but centers the text
'Hello'.center(30,'!') # '!!!!!!!!!!!!Hello!!!!!!!!!!!!!'

# To strip off white space characters like spaces or tabs, I can use strip(), rstrip() and lstrip() 
span = 'Hello'.rjust(10) # '     Hello'
span = span.strip() # 'Hello'
'        x       '.strip() # 'x'
'        x       '.lstrip() # 'x         '
'        x       '.rstrip() # '         x'
#I can pass these methods an argument as to what to strip as well
'SpanSpanBaconSpanEggsSpanSpan'.strip('napS') #'BaconSpanEggs' still has Span because it removed these letters up to the first character that wasnt passed to strip

#the replace() string method takes 2 args
#1st arg is a string to look for and
#2nd arg is a string to replace it with.
span = 'Hello there'
span.replace('e','xyz') #'Hxyzllo thxyzrxyz'

#The pyperclip Module has a copy and paste function that can send text to and recieve text from my computers clipboard
#So sending the output of my program to the clipboard will make it really easy to paste it to an email or to a word processor software or some other program
import pyperclip
pyperclip.copy("blah")
pyperclip.paste()

#Formatting string
name = 'john'
place = 'paris'
food = 'pizza'
#Instead of doing this:
'Hello ' + name + 'Lets go to' + place + ' and eat some' + food
#instead of that, I can do this using conversion specifiers
blah = 'Hello %s Lets go to %s and eat some %s' % (name, place,food)
print(blah)

