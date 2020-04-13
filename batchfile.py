#Batch files (also called Shell scripts) let me run multiple commands by just running the batch file.
#Batch file is just a text file with the commands saved to a file that ends with .bat

#first line here runs my python script. second line tells windos to stop
# the @ symbol tells windows ' I dont want you to display this entire line when I run this program. I just want you to do it."
# the percent asterisk tells window "oh yeah forward any command line arguments to the python program"
@py C:\Users\Dan\Desktop\PythonScripts\helloworld.py %*
@pause
#pause is so that cmd window doesnt instantly dissapear on me
