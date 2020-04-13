#like a list, a dictionary is a collection of many values
# but unlike list indexes, indexes for dictionaries can use many different data types not just integers

#index for dictionaries are called keys and a key has an associated value. Its called key/value pair

#index is typed with { }  and accessed with [ ]
myCat = {'name': 'tom' , 'color': ' red', 'disposition': 'loud'  }
myCat['name'] # tom

'my Cat has ' + myCat['color'] + 'Fur' #my Cat has red Fur


#I can still use integer values as keys just like lists use integers for indexes but they dont have to start at 0 and they can be any number
span = {12345: ' Luggage combo' , 42: 'The Answer'}

#Unlike lists, items in dictionaries are unordered  e.g:
# in a list, the first item would be accessed by span[0] but theres no "first item" in a dictionary
[1,2,3] == [3,2,1] #retursn False since the orders arent the same

eggs = { 'name': 'sophie', 'species': 'cat', 'age': 8}
ham = {  'species': 'cat', 'age': 8, 'name': 'sophie', }
eggs == ham # True because theres no order to dictionaries

# To check if a key exists in a dictionary, I can use in and not in e.g:
'name' in eggs #True
'name' not in eggs #False

# Dictionaries are mutable like lists
#Variables hold referneces to dictionary values. Variables dont actually hold the dictionary value itself

# Dictionar methods are:
#keys()
list(eggs.keys())   #['name', 'species', 'age']   #reason im passing this to list() is because if I didnt pass it in list() then these methods return a list like data type which is dict_keys so if I want an actual list value of the keys, I have to pass that value to the list function and that returns a list value

#values()
list(eggs.values())   #['sophie', 'cat', 8]

#items() where it returns a list of 2 item tuples of the key for the first item and value as a second item
# Tuples are basically the exact same thing as lists except they're immutable and they use parentheses
list(eggs.items())  #[('name', 'sophie'), ('species', 'cat'), ('age', 8)]

#I can use these methods in for loops:
for k in eggs.keys():
    print(k)   #name species age

for v in eggs.values():
    print(v)   #sophie cat 8

#I can use the multiple assignment trick and have multiple variables in the for loop for the items:
    for k,v in eggs.items():  # name sophie  species cat    age 8 
        print(k,v)

for i in eggs.items():
    print(i)   #prints tuples:  ('name', 'sophie') ('species', 'cat') ('age', 8)

#I can use  'in' to check if theres a specific value in the dictionary e.g:
'cat' in eggs.values()  #True


#Its super tedious to check whether a key exists in a dictionary before accessing the key value  so if I do:
#   eggs['color'] #returns a huge error so I can instead do this:
if 'color' in eggs:
    print(eggs['color']) #will only print IF theres actually 'color' key in eggs. It wont show the huge error even if the key doesnt exist
#But ITS REALLY TEDIOUS DOING if statement every time
# So pyhon gives me a get() method that takes 2 arguments.
    #1st arg is key of the values I want to retrieve
    #2nd arg is a fallback default value that the method returns if that key doesnt exist in the dictionary
eggs.get('age',0) # returns 8 because the dictionary has the key of age
eggs.get('color',' ') # returns ' ' since theres no key called color in eggs dictionary

picnicItems= { 'apples': 5, 'cups' : 10}
print('I am bringing ' + str(picnicItems.get('apples',0)) +' apples and also bringing ' +  str(picnicItems.get('napkins',0) )+ ' napkins')

#I often have to set a value in a dictionary for a certain key, only if that key doesnt have a value. 
#Opposite of .get() method is the .setdefault() method. .setdefault() takes 2 args. 1st arg is the key, 2nd arg is the value I want they key to 
#setdefault() is a nice shortcut to determine if a key exists
# I can do this:
if 'color' not in eggs:
    eggs['color'] = 'black'
# all in just one line of code:
eggs = { 'name': 'sophie', 'species': 'cat', 'age': 8}
eggs.setdefault('color','black') # I want to set the color key only if its not already set, so that it defaults to black
eggs #{'name': 'sophie', 'species': 'cat', 'age': 8, 'color': 'black'}
#since the color key already exists, if I do setdefault but change the value, it STILL wont change!! e.g:
eggs.setdefault('color','pink')
eggs # {'name': 'sophie', 'species': 'cat', 'age': 8, 'color': 'black'}


import pprint   #pprint makes the print look cleaner

message = '''adjsajdbnasa

        bndsDASDF


S'''    #if I use three quotes '''  to open and end a string, I can format it in any way!
count = {}

for character in message.upper():
    count.setdefault(character,0)  #adds letter seen for the first time as a key and defaults its value to 0
    count[character] = count[character] + 1

pprint.pprint(count)

#to have it printed as a string instead of printed to the shell, I can use pprint.format e.g:
text = pprint.pformat(count)

print(text)


#to see what type something is, I can use the type() function e.g:
type(42) #int
type('asda') #string
type(eggs) #dictionary
