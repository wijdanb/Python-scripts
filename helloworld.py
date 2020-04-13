#! python3
import sys

#first line of my python programs should be a shebang line which tells my computer
#that I want python to execute this program. Shebang starts with #!
#on windows its #! python3

print('hello world')

 
 
#Batch files (also called Shell scripts) let me run multiple commands by just running the batch file.
#Batch file is just a text file with the commands saved to a file that ends with .bat

#first line here runs my python script. second line tells windos to stop
# the @ symbol tells windows ' I dont want you to display this entire line when I run this program. I just want you to do it."
# the percent asterisk tells window "oh yeah forward any command line arguments to the python program"

#instead of doing py I can instead do pyw which runs a windowsless pythong that doesnt make the cmd line window appear at all
#    @py C:\Users\Dan\Desktop\PythonScripts\helloworld.py %*
#   @pause
#pause is so that cmd window doesnt instantly dissapear on me

#Its annoying to run this in the cmdline because I have to type the entire path,  
# so I can shorten it to typing hello(I dont need to do .bat since windows knows)
#   by adding my pythonscripts folder to the PATH environment variable
#Enviroment variables are kind of like variables for my operating system.
#All the major operating systems use environment variables, in particular one called PATH which is just a list of folders
#Right now if I just type in hello in the cmd run, it wont know what folder to look at but I can add my pythonscripts foler to the PATH and that will make windows check it for any hello.bat files

#To add my pythonscripts folder to PATH:
#Go to control panel
#Go to system and security
#Go to system
#Go to advanced system settings
# On the Advanced tab, click on Environment Variables
#Under where it says system variables, look for Path, click on it then click on Edit
# Click New and copy and paste the path of the pythonscripts

#Now I can run hello in run cmd and it runs the code

# Command line arguments are typed when I run my program e.g in the command line run:
#if I ran hello and I specify some cmd line args right here and seperate them with spaces:
# hello arg1 arg2 arg3

#These cmd line arguments, also called cmd line options, can be accessed in my code as a list of strings stored in the sys.argv variable
#I need to import the sys module: import sys
# then print out that list by calling:
print(sys.argv) #sys.argv is a list value of strings, one string for each cmd line argument
# this is handy if I have to specify some extra added additional information when I run my program
# thats the reason I needed the %* in the hello.bat file because normally, when I'm typing out those args on the cmdline run, its actually passing those cmd line args to the hello.bat file so the %* tells the batch file to forward them to this helloworld.py file.

