import pprint   #pprint makes the print look cleaner

message = '''adjsajdbnasa

        bndsDASDF


S'''    #if I use three quotes to open and end a string, I can format it in any way!
count = {}

for character in message.upper():
    count.setdefault(character,0)  #adds letter seen for the first time as a key and defaults its value to 0
    count[character] = count[character] + 1

pprint.pprint(count)

#to have it printed as a string instead of printed to the shell, I can use pprint.format e.g:
text = pprint.pformat(count)

print(text)
