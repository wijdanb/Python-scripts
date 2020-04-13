#I can write a simple script that automatically launches the browser to a specific address on google maps
#it would be cool if I could run this program and the cmd line args would be the address

import webbrowser, sys, pyperclip

sys.argv #would have the cmd line args e.g ['mapit.py', '870', 'Valencia', 'St.']

#check if cmd line arguments were passed
if len(sys.argv) > 1:
    #['mapit.py', '870', 'Valencia', 'St.'] to '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else: #assuming user has the address on their clipboard
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)

#I'm gonna create a batch file to make it super easy to run this script. Its the mapit.bat
#then in cmd run I type: mapit 870 Valencia St.
#If i have the address copied on my clipboard, I can instead in cmd run type: mapit
