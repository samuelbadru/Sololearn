# Functions

# 38.2: Complete the code to remove the smallest and largest elements from the data set you're analysing and output the sum of the remaining numbers.
data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]

min = min(data)
max = max(data)
data.remove(min)
data.remove(max)

sum = 0
for i in data: 
 sum += i
 
print(sum)

# 39.2: Your friend is sending you a text message, however his caps lock is broken and the whole message is in uppercase. Make a program to convert text to lowercase.
text = input()
print(text.lower())

# 41.2: Make a function that converts a foot value to inches.
def convert(feet):
    print(feet * 12)

feet = int(input())
convert(feet)

# 42.2: Write a function that takes a string and a letter as its arguments and returns the count of the letter in the string.
def letter_count(text, letter):
    count = 0
    for i in text:
        if i == letter:
            count += 1
    return count

text = input()
letter = input()

print(letter_count(text, letter))

# 45: Code project - Make a search enginge where the given code takes a text and a word as input and passes them to a function called search(), which tells you if the word is found in the text. 
text = input()
word = input()

def search(text, word):
 if word in text:
  return "Word found"
 else:
  return "Word not found"

print(search(text, word))