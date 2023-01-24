# More Types

# 53.2:  using the inventory management program, how many apples are in the store?
store = {"Orange": 2, "Watermelon": 0, "Apple": 8, "Banana": 42}

print(store["Apple"])


# 54.2: use the .get() method instead of the if/else statement, with a deafult value of "Book not found"
books = {
    "Life of Pi": "Adventure Fiction", 
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics", 
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}

book = input()
print(books.get(book, "Book not found"))

# 55.2: Find the distance between the two coordinates given
'''The linear distance is the square root of the square of the horizontal distance plus the square of the vertical distance between two points.'''
import math

p1 = (23, -88)
p2 = (6, 42)

distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

print(distance)

# 56.2: Output the last element of the list
x = input()
elements = x.split()

print(elements[-1])


# 57.2: Write a program to take a number as input, and output a list of all the numbers below that number, that are a multiple of both, 3 and 5.
x = int(input()) 
list = [i for i in range(x) if i % 3 == 0 and i % 5 == 0]
print(list)


# 58.2: generate the output "name is age years old".
name = input()
age = int(input())

print(f"{name} is {age} years old")


# 59.2: Replace all of the # characters with spaces and output the result.
txt = input()
print(txt.replace("#", " "))


# 60.2: Given text as input, output the number of words it contains.
txt = input()
print(len(txt.split()))

# 62: Code Project - Given a text as input, find and output the longest word.
txt = input()
words = txt.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)
