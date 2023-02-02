# Working with strings

# 3.2: Count the number of vowels in any given text
text = input()

count = 0

for c in text:
    if c in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print(count)


# 4.2: Output each letter of the string on a new line, repeated N times, where N is the position of the letter in the string. 
text = input()

position = 1

for c in text:
    print(c * position)
    position += 1


# 5.2: Make a text editor with find/replace functionality, while also showing the number of replacements made.
text = "Amy has 128 dollars, while David has 54 dollars. Amy is going to the zoo. David watches soccer."

find = input()
replace = input()

print(text.count(find))
print(text.replace(find, replace))


# 7: Code Project - Create a letter frequency whole percentage calculator
text = input()
letter = input()

print(int(text.count(letter)/len(text) * 100))
