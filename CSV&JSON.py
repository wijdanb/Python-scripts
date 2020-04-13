#Working with CSV files

"""
CSV files are simple, lacking many of the features of an Excel spreadsheet. For example, CSV files:

Don’t have types for their values—everything is a string
Don’t have settings for font size or color
Don’t have multiple worksheets
Can’t specify cell widths and heights
Can’t have merged cells
Can’t have images or charts embedded in them
The advantage of CSV files is simplicity. CSV files are widely supported by many types of programs, can be viewed in text editors (including Mu), and are a straightforward way to represent spreadsheet data. The CSV format is exactly as advertised: it’s just a text file of comma-separated values.

Since CSV files are just text files, you might be tempted to read them in as a string and then process that string using the techniques you learned in Chapter 9. For example, since each cell in a CSV file is separated by a comma, maybe you could just call split(',') on each line of text to get the comma-separated values as a list of strings. But not every comma in a CSV file represents the boundary between two cells. CSV files also have their own set of escape characters to allow commas and other characters to be included as part of the values. The split() method doesn’t handle these escape characters. Because of these potential pitfalls, you should always use the csv module for reading and writing CSV files.
"""

#To read data from a CSV file with the csv module, you need to create a reader object. A reader object lets you iterate over lines in the CSV file. Enter the following into the interactive shell, with example.csv in the current working directory
#The csv module comes with Python, so we can import it ➊ without having to install it first.
import csv
import os
print(os.getcwd())
os.chdir('C:\\Users\\Dan\\Documents')

exampleFile = open('example.csv')
#To read a CSV file with the csv module, first open it using the open() function ➋, just as you would any other text file. But instead of calling the read() or readlines() method on the File object that open() returns, pass it to the csv.reader() function ➌. This will return a reader object for you to use. Note that you don’t pass a filename string directly to the csv.reader() function.
exampleReader = csv.reader(exampleFile)
#The most direct way to access the values in the reader object is to convert it to a plain Python list by passing it to list() ➍. Using list() on this reader object returns a list of lists, which you can store in a variable like exampleData. Entering exampleData in the shell displays the list of lists ➎.
exampleData = list(exampleReader)
print(exampleData)
#Now that you have the CSV file as a list of lists, you can access the value at a particular row and column with the expression exampleData[row][col], where row is the index of one of the lists in exampleData, and col is the index of the item you want from that list. Enter the following into the interactive shell:
print(exampleData[0][0]) #4/5/2015 13:34:02
print(exampleData[0][1])  #Apple


#Reading Data from reader Objects in a for Loop

#For large CSV files, you’ll want to use the reader object in a for loop. This avoids loading the entire file into memory at once. For example, enter the following into the interactive shell:
import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
#After you import the csv module and make a reader object from the CSV file, you can loop through the rows in the reader object. Each row is a list of values, with each value representing a cell.
#The reader object can be looped over only once. To reread the CSV file, you must call csv.reader to create a reader object.
for row in exampleReader:
#The print() function call prints the number of the current row and the contents of the row. To get the row number, use the reader object’s line_num variable, which contains the number of the current line.
    print('Row#' + str(exampleReader.line_num) + ' ' + str(row))


#writer objects
# A writer object lets you write data to a CSV file. To create a writer object, you use the csv.writer() function. Enter the following into the interactive shell:
import csv
#First, call open() and pass it 'w' to open a file in write mode ➊. This will create the object you can then pass to csv.writer() ➋ to create a writer object.
#On Windows, you’ll also need to pass a blank string for the open() function’s newline keyword argument. For technical reasons beyond the scope of this book, if you forget to set the newline argument, the rows in output.csv will be double-spaced, as shown in Figure 16-1.
outputFile = open('output.csv','w',newline='')
outputWriter = csv.writer(outputFile)
#The writerow() method for writer objects takes a list argument. Each value in the list is placed in its own cell in the output CSV file. The return value of writerow() is the number of characters written to the file for that row (including newline characters).
outputWriter.writerow(['spam,', 'eggs','bacon','chicken'])
#Notice how the writer object automatically escapes the comma in the value 'Hello, world!' with double quotes in the CSV file. The csv module saves you from having to handle these special cases yourself.
outputWriter.writerow(['Hello, world!','eggs','blah','cheese'])
outputWriter.writerow([1,2,3,4,5,6,7,8.4242])                      
outputFile.close()

#.tsv files
#The delimiter and lineterminator Keyword Arguments
#Say you want to separate cells with a tab character instead of a comma and you want the rows to be double-spaced. You could enter something like the following into the interactive shell:
import csv
csvFile=open('example.tsv','w',newline='')
#This changes the delimiter and line terminator characters in your file. The delimiter is the character that appears between cells on a row. By default, the delimiter for a CSV file is a comma. The line terminator is the character that comes at the end of a row. By default, the line terminator is a newline. You can change characters to different values by using the delimiter and lineterminator keyword arguments with csv.writer().
#Passing delimiter='\t' and lineterminator='\n\n' ➊ changes the character between cells to a tab and the character between rows to two newlines. We then call writerow() three times to give us three rows.
csvWriter = csv.writer(csvFile,delimiter='\t',lineterminator='\n\n')
csvWriter.writerow(['apples','oranges','graphs'])
csvWriter.writerow(['eggs','milk','grapes','bones'])

csvWriter.writerow(['spam','spam','spam','spam'])

csvFile.close()


#DicReader and DictWriter CSV objects
#For CSV files that contain header rows, it’s often more convenient to work with the DictReader and DictWriter objects, rather than the reader and writer objects.
#The reader and writer objects read and write to CSV file rows by using lists. The DictReader and DictWriter CSV objects perform the same functions but use dictionaries instead, and they use the first row of the CSV file as the keys of these dictionaries.
import csv
exampleFile = open('example_header.csv')
exampleDictReader = csv.DictReader(exampleFile)
#Inside the loop, DictReader object sets row to a dictionary object with keys derived from the headers in the first row. (Well, technically, it sets row to an OrderedDict object, which you can use in the same way as a dictionary; the difference between them is beyond the scope of this book.) Using a DictReader object means you don’t need additional code to skip the first row’s header information, since the DictReader object does this for you.
for row in exampleDictReader:
    print(row['Date'], row['Fruits'], row['Quantity'])

#If you tried to use DictReader objects with example.csv, which doesn’t have column headers in the first row, the DictReader object would use '4/5/2015 13:34', 'Apples', and '73' as the dictionary keys. To avoid this, you can supply the DictReader() function with a second argument containing made-up header names:
import csv
exampleFile = open('example.csv')
#Because example.csv’s first row doesn’t have any text for the heading of each column, we created our own: 'Date', 'Fruits', and 'Quantity'.
exampleDictReader = csv.DictReader(exampleFile,['Date','Fruits','Quantity'])
for row in exampleDictReader:
    print(row['Date'],row['Fruits'], row['Quantity'])


#DictWriter objects use dictionaries to create CSV files for headers
import csv
outputFile = open('output.csv','w',newline='')
#If you want your file to contain a header row, write that row by calling writeheader(). Otherwise, skip calling writeheader() to omit a header row from the file. You then write each row of the CSV file with a writerow() method call, passing a dictionary that uses the headers as keys and contains the data to write to the file.
outputDictWriter = csv.DictWriter(outputFile,['Name','Pet','Phone'])
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name' :'Joe','Pet': 'dog','Phone': '7855-12646231'})
outputDictWriter.writerow({'Pet': 'Giraffe','Phone':'38213214','Name':'Craaaig'})
outputFile.close()

#Ideas for programs:
"""Compare data between different rows in a CSV file or between multiple CSV files.
Copy specific data from a CSV file to an Excel file, or vice versa.
Check for invalid data or formatting mistakes in CSV files and alert the user to these errors.
Read data from a CSV file as input for your Python programs. """




 

































