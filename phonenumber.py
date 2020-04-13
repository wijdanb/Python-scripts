
import re
batRegex = re.compile(r'Bat(wo)*man')  #? Says that wo can appear in the text 0 or 1 times in order to match this pattern
mo = batRegex.search('The Adventures of Batman')
mo.group() #’Batman’
mo = batRegex.search('The Adventures of Batwoman')
mo.group() #’Batwoman’
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search(' My hpone number is 555-1212')
print(mo.group())


haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('HaHaHaHaHaHaHaHa')
print(mo.group())

numbers = '445-423-4231 and then the other number might be 332-441-5234 and then its also 963-321-555'

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(numbers))

beginsWithHelloRegex = re.compile(r'^Hello') #the string MUST begin with Hello, not in the middle or not at the end
beginsWithHelloRegex.search('Hello there!') #returns a Matched Object
beginsWithHelloRegex.search('Ohhhhh Hello there!') == None #True because Hello is NOT at the start of the string


endsWithWorldRegex = re.compile(r'World!$')
print(endsWithWorldRegex.search('This is the World!'))  #returns a Matched object with 'World!'


import re
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub(' REDACTED','Agent Alice gave docs to Agent Bob')



re.compile(r'''
\d\d\\d
-
\d\d\d
-
\d\d\d\d''',re.VERBOSE)

