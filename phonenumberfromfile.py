#! python3
import re,pyperclip

#create a regex for phone numbers
phoneRegex = re.compile(r'''
# could be 415-444-2212 or (415) -322-4123, or 555-000 ext 12345, ext.1234,x2134
(                    #im putting everything into a group because im gonna be using findall and since its a tuple, I need to put everything inside one larg group that way group0, the very first group is going to cover the entire matched text 
((\d\d\d) | (\(\d\d\d\) ) )?               #area code(optional)
(\s|-)                                           #first seperator
\d\d\d                                          #first 3 digits
-                                                 #seperator
\d\d\d\d                                        #last 4 digits
(((ext(\.)?\s) |x)                             #extension word-part(optional)
 (\d{2,5}))?                                  #extension number-part(optional)
)

''',re.VERBOSE)

#Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@some.+_thing.com    efrancis@optonline.net
[a-zA-Z0-9_.+]+       #name part
@                      #@ symbol
[a-zA-Z0-9_.+]+        #domain name part
''',re.VERBOSE)


#Get text off the clipboard
text = pyperclip.paste()   #returns the string of the text thats currently on the clipboard so i save it into text

#Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)  #findall returns a list of strings for us with each string being a matched phone number
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
        allPhoneNumbers.append(phoneNumber[0])

print(extractedEmail)
print(allPhoneNumbers)

#Copy the extracted email/phone to the clipboard
#join takes a list of strings and it joins them together in a single string and this string will be in between each of the strings in this list. Ill have a \n between all of the phone numbers in this list of phone numbers
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results) #now all of that is saved on my clipboard
