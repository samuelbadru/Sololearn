# Functional Programming

# 64.2: Change the code to calculate the cube of the input and output it.
x = int(input())
y = (lambda z:z**3)(x)
print(y)
#or
x = int(input())
y = lambda z:z**3
print(y(x))

# 65.2: Given a list of names, output a list that contains only the names that consist of more than 5 characters.
names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]
res = list(filter(lambda x: len(x) > 5, names))
print(res)

# 66.2: Given a string as input, create a generator function that splits the string into separate words and outputs the resulting list.
txt = input()
def words(x):
    y = x.split()
    for i in y:
        yield i
print(list(words(txt)))

# 67.2: Add the uppercase_decorator to make the text uppercase.
text = input()

def uppercase_decorator(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper
    
@uppercase_decorator    
def display_text(text):
    return(text)
    
print(display_text(text))

# 68.2: Change the code to calculate and output the sum of the squares of all the list items.
def calc(list):
    if len(list)==0:
        return 0
    else:
        return list[0]**2 + calc(list[1:]) 

list = [1, 3, 4, 2, 5]
x = calc(list)        
print(x)

# 69.2: Given two sets, find and output all the elements that are common to both sets.
set1 = {2, 4, 5, 6}  
set2 = {4, 6, 7, 8, 11, 42, 2}  

print(set1 & set2)

# 70.2: You are given a list of items, and need to find all the possible orders of the items.
from itertools import permutations

items = ['x', 'y']

print(list(permutations(items)))

# 72: Code Project - Write a program to take N (variable num in code template) positive numbers as input, and recursively calculate and output the first N numbers of the Fibonacci sequence (starting from 0).
num = int(input())


def fibonacci(n):
	if n <= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

for i in range(num):
	print(fibonacci(i))
