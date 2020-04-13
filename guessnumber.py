import random

myNumber = 0
myGuess = 0


try:
    print('Hi, whats your name?')
    myName = input()
    if myName.isdigit():
        raise ValueError
    
    
    myNumber = random.randint(1,20)

    print('Well' + myName + 'I am thinking of a number between 1 and 20. Take a guess')
    for i in range(6):
        myGuess = int(input())
        if myGuess == myNumber:
            print('You got it!')
            break
        elif myGuess < myNumber:
            print('The number you guessed is too low')
            continue
        elif myGuess > myNumber:
            print('The number you guessed is too high')
            continue
except:
    print('Please input words for your name and an integer for a guess')
