

#If I want my data to persist, I need to save it to a file .
#I can think of a files contents as a single string value. If a file is GB in size, this string will be billions of characters long



#files have 2 key properties: Filenames and File paths
#Root folder in windows is C:\
#On windows the folder seperator is \ but in Mac  & Linux is /

#I'll be using strings to represent file paths and file names
#To have a literal backslash, I need to escape the backslash itself: '\\' to make \ OR I can just use raw strings

#IF i have a whole bunch of names for different folders like:  ['folder1', 'folder2', 'folder3', 'file.png'] I could just use the .join() string method to create a file path string out of all these individual folders and file names:
# '\\'.join(['folder1', 'folder2', 'folder3', 'file.png']) #'folder1\\folder2\\folder3\\file.png'  BUT THIS ONLY WORKS ON WINDOWS
#Ideally, I want all my python scripts to work on all operating systems so python has a module called os

import os
#os module contains alot of different file path related functions that I can use.
# os.path.join() is a join function thats inside a path module thats inside the os module that takes several string arguments  and returns the string value of a path thats appropriate for the operating system that im running on
os.path.join('folder1', 'folder2', 'folder3', 'file.png')  #'folder1\\folder2\\folder3\\file.png' 
#os.sep is the value of the seperator so os.sep on windows returns '\\'

#every program has a setting called current working directory. directory is an older name for folder
#the current working directory tells the program what folder it should look in when we just hand it a file name without a file path
#to get the current working directory as a string value its: os.getcwd()
os.getcwd() #'C:\\Users\\Dan\\Desktop\\PythonScripts'
#to change current working directory its: os.chdir() and I pass it a new filepath e.g:  os.chdir('c:\\') basically I changed the cwd to the root file folder

#2 kinds of filepaths:
    #1. Absolute file path - always begins with the root folder. It gives me the complete location of a program e.g: 'c:\\folder\\folder2\\spam.png
    #2. Relative file path- do not begin with the root folder. always going to be relative to the current working directory. It wont begin with the root folder e.g: 'folder1\\folder2\\spam.png' and its going to assume that this relative filepath means its inside the root folder c:\\
            # . and .. are special names that can be used in a relative file path
                # .\ stands for this directory/folder
                # ..\ stands for the parent directory/folder
                
# os.path.abspath() returns string of an absolute path of the path that I pass it e.g os.path.abspath('spam.png') returns 'C:\\Users\\Dan\\Desktop\\PythonScripts\\spam.png'   or os.path.abspath('..\\..\\spam.png') returns 'C:\\Users\\Dan\\spam.png'
#os.path.isabs() lets me pass it any file path I want and will return true if this is an absolute path. Basically a simple way to programatiically determine if something begins with a root folder e.g  os.path.isabs('..\\..\\spam.png') returns False   or os.path.isabs('c:\\folder\\folder') returns True
# os.path.relpath() gives me the relative file path to the given file path(1st arg) from the start path(2nd arg) e.g os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')  returns 'folder2\\spam.png'

#os.path.dirname() retrieves the directory part e.g
    #os.path.dirname('c:\\folder1\\folder2\\spam.png') returns 'c:\\folder1\\folder2'
#os.path.basename() retrieves the last part after the set of final slashes e.g
    #os.path.basename('c:\\folder1\\folder2\\spam.png') returns 'spam.png'   This also works for folders e.g os.path.basename('c:\\folder1\\folder2') returns 'folder2'

# os.path.exists() checks the files on my hard drive. I can pass it a file path and returns True if this file actually exists and false if it doesnt  e.g:
os.path.exists('c:\\folder1\\folder2\\spam.png') #False
os.path.exists('c:\\windows\\system32\\calc.exe') #True

#os.path.isfile() checks if its a file name e.g
os.path.isfile('c:\\windows\\system32\\calc.exe') #True
os.path.isfile('c:\\windows\\system32') #False because its a folder

#os.path.isdir() checks if its a folder name
os.path.isdir('c:\\windows\\system32\\calc.exe') #False
os.path.isdir('c:\\windows\\system32') #True

#os.path.getsize() returns the size in bytes as an int for a file I pass in e.g:
os.path.getsize('c:\\windows\\system32\\calc.exe') #26112
#os.listdir() returns a list of strings with the file names and folder names that are inside the path of the folder I pass it:
os.listdir('c:\\Users') #['All Users', 'Dan', 'Default', 'Default User', 'Default.migrated', 'desktop.ini', 'Public']

#Example code of combining os.path.getsize() and os.listdir to finding the total size of all files in a folder
totalSize = 0
for filename in os.listdir('C:\Program Files (x86)'):   #for loop that iterates over the files returned by os.listdir. This listdir will also contain folder names as well as file names BUT I JUST WANT to look at the file names so I have some code that checks its a file and in the .isfile I have to provide it the full path so thats why I .join it . If its NOT a filename then I continue the loop otherwise I add the file size to the totalSize
    if not os.path.isfile(os.path.join('C:\Program Files (x86)', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\Program Files (x86)', filename))

print(totalSize)

#os.makedirs() is to create new folders. I can pass it a relative or absolute file path and it will create all the folders I specify
#os.makedirs('C:\\Users\\Dan\\Desktop\\PythonScripts\dogfolder\\andAnotherfolder\\andYetAgainANOTHERFOLDER')



#Now that I know about filenames and file paths, I can start writing strings to files that I create.
    #This is a great way to save information to the hard drive
    #I can then later read these files or any file on the hard drive back into my program
    #just like saving documents
#The types of file that will be reading and writing are called:
    # Plaintext - these files only contain basic text characters and dont include any information about font or size or color
        # end in .txt extension
        # python scripts are an example of plain text files except they also have the .py file extension
        # Plaintext files can be open with text editor programs e.g notepad, textedit etc
        
    # Binary files
        # These are every other type of file e.g word processing docuemtns, pdfs, images, spreadsheets, executable programs,
        # Since every different type of binary file has to be handled in it sown way, I wont go into reading and writing raw binary files directly. Most of the time, there are modules to handle these binary file formats for me and ill use them later on
        
# 3 steps to reading and writing files in Python
    #1. I call the open() function. I pass it a file name that I'd like to open
        #default mode for open() is read mode
        #when a file is open in read mode, python only lets me read/get data from the file BUT NOT WRITE OR MODIFY it
        # open() returns a file object so I save it to a variable
helloFile = open('C:\hello.txt')
        #file datatype has several methods: read()
helloFile.read()
# to close the file, I do .close()
helloFile.close()
#I can only read a file once. To read it again, I need to open it again so:
helloFile = open('C:\hello.txt')
content = helloFile.read()
print(content)
helloFile.close()

# readlines() method for file objects. returns all of the lines as strings inside of a list. Just a different way of getting the file contents in a structure that I want
helloFile = open('C:\hello.txt')
helloFile.readlines()  #['hello world']
helloFile.close()
# .read() returns a single string ,  readlines() returns a list of strings

#Python allows me to write content to files in a similar way to how the print function writes strings to the screen
#I cant write to a file that I've already opened in read mode, instead I open it in Write mode or Append mode
#Write mode will overwrite an existing file and start from scratch with a blank text file
#To open in Write mode I pass it a 'w' as second argument
# Write mode deletes the original contents of the file
helloFile = open('C:\hello.txt','w')
# To write strings to this file I call the write() method and pass  it a string. write() returns the int of how many bytes of how many characters it wrote to it
helloFile.write('blah blah') #9

#Append mode will append the text that im writing to at the end of an existing file. To open a file in append mode, I pass it an 'a' string as second arg
# append mode doesnt delete original content, it adds to it. 
helloFile = open('C:\hello.txt', 'a')
helloFile.write('blah blah yet again') 
#if the file I pass into open() doesnt exist, then python will create a new blank text file for me to write to

# Writing and reading text files is a good way to store a single long string
#but if I want to store variables that have lists and dictionaries and other complex data structures, I can save variables in my python programs to binary shelve files using the shelve module
import shelve
shelfFile = shelve.open('mydata') #open() is a shelve method that returns a shelf file objext
#I can make changes to the shelve value as if it were a dictionary and when im done, I call close on the shelf value e.g:
shelfFile['cats'] = ['Sophie','pooka','garfield'] #im saying that shelfFile has a key 'cats' that stores a list of cat names
shelfFile.close()
#Then later when I run this program again in the future, I can have code that reopends the shelfFile and can grab the values, just like a dictionary
shelfFile = shelve.open('mydata')
shelfFile['cats']   #['Sophie', 'pooka', 'garfield']

#If I think about it, variables inside of Python programs are kind of like key/value pairs in a dictionary e.g if I did:
cats = ['Sophie','pooka','garfield']  #cats variable is kinda like the key that stores the values and thats why shelve has a dictionary like structure
#The benefit of using the shelve module is that I can store things like list and dictionaries and non-text data to a file and then reopen them in the future with my python program
shelfFile.close()
#so shelve module is storing all shelve file objects in my current working directory" C:\Users\Dan\Desktop\PythonScripts
# there are 3 new files in my cwd: mydata.bak, mydata.dat, mydata.dir and these files is where the information of the shelve is all stored
# these 3 files are  binary files 

#shelf file objects are very similar to dictionaries
    #they even have keys() and values() method which return a list like values for all theys and values inside them 
shelfFile = shelve.open('mydata')
shelfFile.keys() #KeysView(<shelve.DbfilenameShelf object at 0x03FDB0B8>)
#convert the keys to a list
list(shelfFile.keys()) #['cats']
list(shelfFile.values()) #[['Sophie', 'pooka', 'garfield']]


#Copying and moving folders
# shutil module has functions that let me copy, move, rename and delete files in my Python programs
import shutil
#shutil.copy() will copy a file to a new folder. 1st arg is the file I want to copy, 2nd arg is where I want to copy the file to
shutil.copy('C:\\copy.txt', 'C:\\copyFolder')
# I can also copy and RENAME at the same time by specifying a file name for the destination
shutil.copy('C:\\copy.txt', 'C:\\copyFolder\\spamspamspam.txt')

#.copy() function works for copying a single file but what about copying entire folders?
# shutil.copytree() function copys an entire folder. 1st arg is the folder I want to copy. 2nd arg is where I want to copy the folder to and the copy's folder name
#shutil.copytree('C:\\copyFolder', 'C:\\newFolder')
# shutil.move() moves a file from one location to another. 1st arg is the file I want to move. 2nd arg is the location to where I want to move the file
#shutil.move('C:\\joe.txt', 'C:\\copyFolder) #might cause permission error. If so, open up this python shell or ide as administrator
#There is NO RENAME function, instead I use this .move() function and I move the file into the same folder that its in but with a new name
#shutil.copy('C:\\nameFolder\\thisnamesucks.txt', 'C:\\nameFolder\\coolname.txt')


#To delete files and folders, there are 3 functions I can use from the os module:
import os
    # 1. os.unlink() deletes a single file.     I should do os.getcwd() to see where it will look for the file
#os.unlink('bacon.txt')
    # 2. os.rmdir() deletes an empty folder. When I call os.rmdir(), the folder HAS to be completely empty, it cant have any files or folders inside of it
#os.rmdir('C:\\delicious')
    #3 shutil.rmtree() deletes a folder and its ENTIRE contents meaning it deletes all the files and folders inside of it
import shutil
#shutil.rmtree('c:\\delicious')

#Since I can accidently delete files and wont be able to get them back, I should do a DRY run, e.g:
import os
#os.chdir('C:\\Users\\Al\\Desktop')
for filename in os.listdir():
    if filename.endswith('.rxt'): #if i accidently said .rxt instead of .txt files this would cause problems so instead of unlinking the file, I just print it to test it does the right thing
        #os.unlink(filename)  #commenting this because if its done, then it will delete something forever.
        print(filename) #printing the filenames to test it initially. If it passes the test, then I can uncomment os.unlink(filename)

#But these deleting methods are dangerous since it will be permanent.
# However, theres a module I can use called send2trash that instead of deleting it permanently, it will send it to my operating system's recycling bin
# I have to use the pip installer since it doesnt come with python. 
# To install on windows its:
    #win+r to open "Run Dialog"
    # type cmd then press enter
    # change dir to C:\Users\Dan\AppData\Local\Programs\Python\Python38-32\Scripts"
    # then run: pip.exe install send2trash
#Then I can do:
import send2trash
#send2trash.send2trash('c:\\delete')


# If I want to write a code that applies to all of the folders and files inside a specific file, in other words:
# If I want to walkthorugh a folders tree and either rename or copy or do something with all of the files
#Writing code to do this can be tricky but Python provides a function to handle this process for me
#its called os.walk() function
import os
# os.walk() 1st arg is the root folder I want to check. The return value is used in for loops. It returns 3 values on each iteration of the loop
# 1st value (folderName) will be a string with the folder name that im currently looking at  
#2nd value(subfolders) provides a list of all the folders inside that folder
# 3rd value (filenames) contains a list of strings for all the files inside that folder
for folderName, subfolders, filenames in os.walk('C:\\spamfolder'):
    print(' The folder is ' + folderName)
    print(' The subfolders in ' + folderName + 'are' + str(subfolders))
    print(' The filenames in ' + folderName + 'are: ' + str(filenames))
    print()
    for subfolder in subfolders:
        if 'fish' in subfolder:     #if string 'fish' was in the subfolder name, I could delete the folders
            os.rmdir(subfolder) #deletes 'fish' folders
    for file in filenames:
        if file.endswith('.py'):
            #if I had a copy function, add the old name and maybe want to rename it so it had a new extension e.g .backup
            shutil.copy(os.join(folderName,file), os.join(folderName, file + '.backup'))    #file is the string of a file name, NOT an absolute path so I have to call os.join to join the foldername and that file

