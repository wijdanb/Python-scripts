cars = [[1,2,3], ['ferrari','porcshe','bmw']]  #can have a lists of lists

#to get a single value from a list, I can use an index

print(cars[1][0])  #ferrari

#to get the last element, I can pass in a negative value

print(cars[1][-1]) #bmw

print(cars[1][-2]) #porsche

print(cars[1][-3]) #ferrari


# To get several values from a list, I can slice lists. slice has 2 integers seperated by a colon for the start& end indexes:

# cars[1][1:3] starts at index 1 and goes up to but doesnt include the value at index 3
print(cars[1][1 : 3])  #returns a new list of ['porsche','bmw']

#I can assign a slice t oa  new list that will change the items in the list

span = [10,20,30]

span[1]= 'hello'
span[1:3] = ['Cat','Dog','Tree']

print(span) # span is now ['10','Cat',Dog','Tree']

color = ['gren','blue','red','orange','pink']
# As a shortcut, I can leave out one or both of the indexes on either side of the : in a slice
#leaving out the first index is the same as using 0 or the beggingin of the list
color[:3] #[green,blue,red]

# leaving out the second index is the same as using the length of the list,which will slice to the end of the list
print(color[1:]) # ['blue',red','orange','pink']

# TO DELETE VALUES USE: del
#if I want to delete red from color:
#all of the items after that get moved up one so it doesnt leave any gaps in the list
del color[2]   

print(color)#['gren', 'blue', 'orange', 'pink']

#to get legnth of list, I can do len:
len([1,2,3]) #3
# I can concatonate lists:
[1,2,3]+[4,5,6] # [1,2,3,4,5,6]
#I can also do list replication:
[1,2,3] * 3 # [1,2,3,1,2,3,1,2,3]

#Many of the things I can do with strings, I can also do with lists
#I can think of a string value as a list of single character values.
#Theres a list() function that returns a list form of the value that I pass it:
#  list('Hello')  returns ['H', 'e', 'l', 'l', 'o']  in the shell

#if I need to determine if a value is or isnt in a list, I can use the in and not in operators:
#in and not in are used to connect to values

#in:
#Theres a value that im looking for and then the in operator and then the list value where it might be found
'howdy' in ['hello','howdy','cowboy'] # True when copied into the shell
50 in ['hello','howdy','cowboy'] # False when copied into the shell

#not in:
'howdy' not in ['hello','howdy','cowboy'] # False when copied into the shell
50 not in ['hello','howdy','cowboy'] # True when copied into the shell

#for loops with lists:
# if I do:

range(4) #this returns range(0,4). range objects are a list like values

for i in range(4):
    print(i)
 #is the same as:
for i in [0,1,2,3]:
    print(i)

#list like in these examples means data types that are sequences in python

#to get the list from range I do:
# list(range(4))  this can be handy if I want to get a collection of integers in a list
#so if I wanted a list of numbers from 0-100 but goes up in twos its:
# list(range(0,100,2))  

#common technique in python to do for loops in list is:
# for i in range(len(someList)):
# e.g:
supplies = ['pens','staplers','flamethrowers','binders']
for i in range(len(supplies)):
    print('Index is: ' + str(i) + ' and supply is ' + supplies[i])


# Pythons way of array destructuring is how I do multiple assignments of elements of lists to variables:
cat = ['fat','orange','tony']
#I can now do:
size, color,name = cat   #all in one line

#instead of doing:
size = cat[0]
color = cat[1]
name = cat[2]

#another trick with multiple assignment is that I can have multiple variables on the left side AND also have multiple values on the right side, I just need to seperate the values with commas:
size, color, name = 'small', 'black', 'gary'
#this trick is often used to do swap operations with variables
a = 'AAA'
b = 'BBB'
#if i want to swap a's and b's values I can do it easily with the multiple assignment trick
a , b = b, a

#One more shortcut python has is augmented assignment operators.
#When I assing a value to a variable I'll frequently use the variable itself.  basically +=
span = 42
span += 1 #same thing as span = span + 1

 
#list methods:

# somelist.index() is a function where I pass an argument and then returns the index of where my argument is on the list e.g:
span = ["bob", " jake" ,"kale"]
span.index("kale") # 2
#span.index("ajsdbasbdsa") #ValueError
#if theres copies of the value, it returns the first time it sees the value e.g:
span = ['joe','joe','joe'] #returns 0

#To add new values to a list, use append() and insert() List methods:

#append() adds the value to the end of a list
span = ['cow','dog','cat']
span.append('moose') #now span has ['cow','dog','cat','moose']

#insert() cab add the value ANYWHERE in the list:
span.insert(1,'chicken') #now span has ['cow','chicken','dog','cat','moose'] everything else gets bumped up

#if i equat the list to .append or .insert it returns a None value so it gets rid of the list entirely
span = span.append('moose') #gets rid of the list
#so the list is modified in place 

# list also has a remove() method where I pass a value that I want removed from the list that its called on:
disease = ['pox','ebola','corona']
disease.remove('pox') #removes pox from the list and now its ['ebola','corona']
#difference with del and .remove() is that with del, I need to give it an index but with .remove(), I give it the value that I want removed

#if theres more than one of the same value I want removed in the list, it removes the first value that matches the value I passed in but not the rest e.g:
animals = ['fox','fox','fox']
animals.remove('fox') # animals list is now: ['fox','fox']


# list with number values or lists with string values can be sorted with sort() method
nums = [509,34,5,29,55]
nums.sort() # now nums is sorted in ascending order [5,29,34,55,509]

#can also sort list that have strings 
animals = ['dog','antelope','cat ']
animals.sort() # ['antelope','cat','dog']

# I can pass in a keyword argument reverse=True to .sort() to change the sorting order
animals.sort(reverse=True) #['dog',cat','antelope']

#I cant sort a list that has both numbers and strings, it returns an error!!!! e.g:
span = [1,2,3,'Alice','Bob']
#span.sort() will cause an error


# technically, .sort() uses ASCII-betical order. Its the same except for UPPercase characters come before lowercase characters
span = ['Alice','Bob','ants','badgers','Carol','Cats']
span.sort() #['Alice','Bob','Carol','ants','badgers',cats] this is weird

#To force the sorting to not put uppercase letters before, I can pass key=str.lower as argument to .sort()
span = ['a','z','A','Z']
span.sort(key=str.lower) #['a', 'A', 'z', 'Z']

#strings and lists are similar if I consider a string to be a list of single character strings
list('Hello') #['H','e','l','l','o']
#I can also do many things with strings like lists e.g indexing, slicing, using them in for loop, len function, not in and in operator,   
name = 'Sophie'
name[0] #'S'
name[1:3] #'op'
name[-2] # 'i'
'So'in name #True
'xxx' in name #false
for letter in name:
    print(letter) # S o p h ie

# THE DIFFERENCE BETWEEN STRINGS AND LISTS IS:
    # Lists are mutable data type   - can have values added, removed or changed
        #when I assign list to a variable, Im actually assignging a list REFERENCE to the variable. Reference is a value that points to some bit of data like a list 
    # Strings are Immutable data type  - cant change or reassign anything in string.
        #immutable can't be modified in place. They can only be replaced by new values
    
#The proper way to modify a string is to create a new string using slices:
name = 'Sophie a cat'
newName = name[0:7] + 'the' +name[8:12]
newName # 'Sophie the cat'

#when I assign list to a variable, Im actually assignging a list REFERENCE to the variable. Reference is a value that points to some bit of data like a list :
span =[1,2,3,4,5]
new = span  #copying the reference to the list, not the list itself
new[3] = 'Hello'
new #[1, 2, 3, 'Hello', 5]
span # [1, 2, 3, 'Hello', 5] #THE SPAN ALSO CHANGES!! Because of reference! This is danger with mutable

#A HUGE bug can happen if I pass a list to a function(copy by reference) e.g:
def eggs(someParam):
        someParam.append('hello')  #i'd assume that someParam will be deleted once I exit the scope but because list is immutable, it actually changed the span!

span = [1,2,3]
eggs(span)
print(span)  #[1, 2, 3, 'hello']   # the local variable someParam changed a variable in the global scope even though I was expecting a pass by copy and not reference!

# To have a completely seperate list that is equal to another lists values I can use: copy.deepcopy() function.
# TO use copy.deepcopy() I need to import copy
import copy
span = ['a','b','c']
cheese = copy.deepcopy(span)
cheese[1]= 'hello'
print(cheese)

# In most cases, the amount of indentation for a line of code in python tells what block its in
#With lists theres an exception, I can do line continuation e.g
span = ['a',
        'b',
        'b',
        'p'
        ]
print(span) #['a', 'b', 'b', 'p']
# To do this even when I dont have lists, I can use : \
print('blah blah blah' +  \
          'blah blah blah')

