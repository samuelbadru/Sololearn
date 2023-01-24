# Regular Expressions

# 83.2: Create a program that will take the phone number as input, and if the number starts with "00", replace them with "+".
import re

number = str(input())

pattern = r"00"

if re.match(pattern, number):
    print(re.sub(pattern, "+", number))
else:
    print(number) 


# 84.2: Write a program that takes a word as input, and outputs "Match" if the word has 4 letters, starts with "m" and ends with "e".
import re

word = input()

pattern = r"m..e"

if re.match(pattern, word):
    print("Match")
else:
    print("No match")


# 85.2: All products have a 4 symbol ID, first two are uppercase characters, and the last two are digits. Write a search tool.
import re
Id = input()

pattern = r"^[A-Z][A-Z][0-9][0-9]$"

if re.match(pattern, Id):
    print("Searching")
else:
    print("Wrong format")


# 86.2: Create a program that takes password as input and returns 'Password created' if it has at least one uppercase character and at least one number.
import re
password = input()

pattern = r"[A-Z]+"
pattern2 = r"[0-9]+"

if re.search(pattern, password):
    if re.search(pattern2, password):
        print("Password created")
    else:
        print("Wrong format")
else:
    print("Wrong format")

# 88.2: Write a program for your research that will take text as input and output all of the hashtags in it separately.
import re
text = input()

pattern = r"#\w+"

hashtags = re.findall(pattern, text)

for i in hashtags:
    print(i)

# 91: Code project - Create a phone number validator where a valid phone number has exactly 8 digits and starts with 1, 8 or 9.
import re

number = input()
pattern = r"^[189][0-9]{7}$"

if re.match(pattern, number):
    print("Valid")
else:
    print("Invalid")
