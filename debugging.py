# Instead of doing try and except, I can also raise my own exceptions
#exception is a way of saying: stop running this code in this function and move the program execution to the except statement
#exceptions are raised with a raise keyword
# im using raise keyword with Exception function
#raise Exception('This is the error message')  #this returns an exception object thats raised #Exception: This is the error message
#so if theres no try and except statement covering the raise statement, the program crashes

'''
*****************
*                   *
*                   *
*****************
'''

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("symbol' needs to be a string of length 1")
    if (width < 2) or (height < 2):
        raise Exception(" 'width' and 'height' must be greater or equal to 2 ")
        
    print(symbol * width)
    
    for i in range(height - 2):
        print(symbol + (' ' * (width -2)) + symbol)
        
    print(symbol * width)
    
#boxPrint('o&^%', 15, 5) #aise Exception("symbol' needs to be a string of length 1") Exception: symbol' needs to be a string of length 1
#boxPrint('*',1,1) #  raise Exception("symbol' needs to be a string of length 1") Exception: symbol' needs to be a string of length 

# The exception shows me a Traceback, which is a call stack and that shows me the lines that were called before getting to the line that caused the error
#I can get the error text as a string value using: traceback.format_exc() function
import traceback
try:
    raise Exception('generic error message')
except:     #lets say that this code is in a program and I dont want the exception to stop the program. I just want it to write the exception text to some sort of log file and then keep the program running
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to error_log.txt')

#Assertion is a sanity check that makes sure my code isnt doing something obviously wrong
#These sanity checks are performed by assert statements
#If the sanity check fails, then an assertion error exception is raised
    # assertion is written by: assert  then followed by a condition. If the condition evaluates to false, then it raises the assertion error
    #assert False, 'This is the error message'  #AssertionError: This is the error message
#in plain english, assert statement is saying:  I asser tthat this condition always holds true and if not, there is a bug somewhere in the program
    #assertions are for programmer errors that are not meant to be recovered from. User errors should raise exceptions 
    #simple data sturcture for a stop light at an intersection on market2nd street:
market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values() , 'Neither light is red!' + str(intersection)
        
print(market_2nd) #{'ns': 'green', 'ew': 'red'}
#switchLights(market_2nd)   uncomment this to do the check
print(market_2nd) #{'ns': 'yellow', 'ew': 'green'} NONE OF THE LIGHTS ARE RED! So I use assert to make sure red is one of the values


    
# logging is a great way to understand whats happening in my program and in what order its happening in
#pythons logging module makes it easy to create a record of custom messages that I write
# logging.basicConfig() function enables the logging module to display log messages on my screen as my program runs
import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -%(levelname)s - %(message)s')
 
#ill make a factorial function that has a bug. the logging should help me see the bug
import logging
#instead of displaying log messages to screen, I can write them to a text file by adding filename = 'filename' in the basicConfig
logging.basicConfig(filename='programminglog.txt', level=logging.DEBUG, format='%(asctime)s -%(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL) #So once i've found the bug and dont need the debugger to log the debug, I can do this turn off all the logging messages. If I want the logging message, I can just comment this entire line
logging.debug('start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):  #this is where the error is. it should start 1 so its: for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' %(i,total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5)) #prints 0 which is wrong
logging.debug('end of program')

#So once i've found the bug and dont need the debugger to log the debug, I can do this turn off all the logging messages:
# 5 levels of log:
    #1. logging.debug()       -lowest   
    #2. logging.info()
    #3. logging.warning()
    #4. logging.error()
    #5. logging.critical()   -highest

# 5 levels of disabling log:
    #1. logging.disable(logging.DEBUG)       -lowest   
    #2. logging.disable(logging.INFO)
    #3. logging.disable(logging.WARNING)
    #4. logging.disable(logging.ERROR)
    #5. logging.disable(logging.CRITICAL) -highest




#Using the debugger
#debugger will run a single line of code and then wait for me to continue

#to enable IDLE's debugger, in the shell, go to Debug > Debugger
#this brings the debug control window. Make sure I check Stack, Source, Locals and Globals checkbox

# Go runs the program normally. It sort of disables the debugger for the rest of the program until it reaches the end of program or a breakpoint
# Step will move the debugger into a function call, if thats whats about to be executed
# Over executes the line of code thats highlighted and proceeds to pause again before it executes the next line
# Out will keep executing lines until the function that I'm currently in returns 
# Quit terminates my program

# To make a breakpoint in IDLE, I right click on a line and Set breakpoint








 
