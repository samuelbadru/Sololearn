# Basic Concepts

# 1.2: print "Python is fun"
print('Python is fun')

# 2.2: Calculate total number of ice cream scoops needed where there are 68 children who get 2 scoops each.
print(68 * 2)

# 5.2: How many miles are in 1000km? (bad question, unclear why floor division is needed)
'''1 mile = 1.6km'''
print(1000 // 1.6)

# 7: Code Project - How much money will you have at the end of 30 days if you get a penny doubled every day.
print(0.01 * 2 ** 30)



# Strings & Variables

# 8.2: Fix the given code to output I'm a programmer. print('I'm a programmer')
print("I'm a programmer")
#or
print('I\'m a programmer')

# 9.2: Print the first 4 letters of the alphabet on separate lines
print('A\nB\nC\nD')

# 10.2: Modify print("ni") to output ni 3 times with an ! at the end
print( "ni" * 3 + "!" )

# 12.2: Raise 7 to the power of 3
x = 7
print(x**3)

# 14.2: If x and y are user inputs, output x y times.
x = input()
y = int(input())
print(x * y)

# 17: Code Project - Make a simple calculator, that takes two integers and outputs their sum
x = int(input())
y = int(input())

print(x + y)



# Control Structures

# 19.2: Write a program that checks if the water is boiling.
temp = int(input())
if temp >= 100:
    print("Boiling")

# 20.2: Write a program to control entrance to an 18+ club.
age = int(input())
name = input()
if age >= 18:
    print("Welcome " + name)
else:
    print("Sorry")

# 21.2: Write a program to check if the given humidity is normal (40 - 60 inclusive)
humidity = int(input())
if 40 <= humidity <= 60:
    print("norm")
#or
humidity = int(input())
if humidity>=40 and humidity<=60:
    print("norm")

# 22.2: Write an ATM program that only accepts Visa or Amex
type = input()
if type == "Visa" or type == "Amex":
    print("accepted")

# 23.2: Write a vending machine program, where the input is the item index and the output is the corresponding item.
fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"]
num = int(input())
if 0 <= num <= 7:
    print(fruits[num])
else:
    print("Wrong number")

# 24.2: Given a list of numbers, output "bingo" if it contains the input number.
items = [42, 88, 721, 12, 43, 22, 908]
num = int(input())
if num in items:
    print("bingo")


# 25.2: Given a list, calculate the middle element's index. (don't understand why this works)
# as list indexing starts at 0, don't need to add 1 to n
items = [2, 4, 6, 8, 10, 12, 14]
print(len(items)//2)

# 26.2: Make a magic box that doubles the count of items you put, every day.
items = int(input())
days = int(input())
i = 1
while i <= days:
    items *= 2
    i += 1

print(items)
#or
items = int(input())
days = int(input())

while days > 0:
    items *= 2
    days -= 1

print(items)

# 27.2: Given a list of numbers, output their sum.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
for i in list:
    sum += i

print(sum)

# 28.2: Write a program that takes a year range and outputs all the dates, excluding the end date given
a = int(input())
b = int(input())

print(list(range(a, b )))

# 30: Code Project - FizzBuzz interview test adaptation, modify code to skip even numbers.
n = int(input())

for x in range(1, n, 2):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)



# Functions & Modules

# 32.2: Personalise the given function
def welcome_message():
	#redesign this function
	name = input()
	print("Welcome, " + name)

welcome_message()


# 33.2: Check if the password and the repeat match
password = input()
repeat = input()

def validate(text1, text2):
    if text1 == text2:
        print("Correct")
    else:
        print("Wrong")

validate(password, repeat)

# 34.2: Create a hashtah generator program for your social network application
s = input()

def hashtagGen(text):
	text = "#" + text.replace(" ", "")	
	return text

print(hashtagGen(s))

# 37.2: Create a dice simulator
import random
random.seed(int(input())) #please don't touch this lane

#generate the random values for every dice
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print(dice1)
print(dice2)

# 40: Code Project - Make a Celsius to Fahrenheit converter
celsius = int(input())

def conv(c):
    c = 9/5 * c + 32
    return c
    

fahrenheit = conv(celsius)
print(fahrenheit)

# Exceptions & Files

# 42.2: Ensure users only enter digits to create their bank PIN codes
pin = input()
try:
	int(pin)
	print("PIN code is created")

except ValueError:
	print("Please enter a number")

# 43.2: Coffee vending machine
coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input())

try:
	print(coffee[choice])
	
except:
	print("Invalid number")
	
finally:
	print("Have a good day")

# 47.2: Accesssing pull ups file record
file = open("/usercode/files/pull_ups.txt")
n = int(input())

print(file.readlines()[n])

file.close()

# 48.2: Write the names to the file
names = ["John", "Oscar", "Jacob"]

file = open("names.txt", "w+")
for name in names:
    file.write(name + "\n")

file.close()

file= open("names.txt", "r")
print(file.read())

file.close()

# 51: Code Project - Make a special book categorization program, which assigns each book a special code based on its title.
'''The code is equal to the first letter of the book, followed by the number of characters in the title.'''
file = open("/usercode/files/books.txt", "r")

for line in file:
    if "\n" in line:
        print(line[0] + str(len(line) - 1))
    else:
        print(line[0] + str(len(line)))
    
file.close()



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


# 73.2 Define a Student class, create an instance, and call its greet method
class Student:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(self.name+" says hi")

obj = Student("John")
obj.greet()

# 74.2 Create a vehicle with a horn method and make a car class that inherits from Vehicle.
class Vehicle: 
    def horn(self):
        print("Beep!")

class Car(Vehicle):
    def __init__(self, name, color):
        self.name = name
        self.color = color

obj = Car("BMW", "red")
obj.horn()

# 75.2 Use operator overloading to add together two bank accounts.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def __add__(self, other):
        return BankAccount(self.balance + other.balance)


a = BankAccount(1024)
b = BankAccount(42)

result = a + b
print(result.balance)


# 77.2 Create a bank account class with a private balance property and a deposit method.
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def __repr__(self):
         return "Account Balance: {}".format(self._balance)
    
    def deposit(self, amount):
        self.amount = amount
        self._balance = self._balance + amount

acc = BankAccount(0)
acc.deposit(int(input()))
print(acc)


# 78.2 Create a calculator class with a static add method
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

        
n1 = int(input())
n2 = int(input())

print(Calculator.add(n1, n2))

# 79.2 Create a number class with an isEven property
class Number:
    def __init__(self, num):
        self.value = num
        
    @property
    def isEven(self):
        if self.value % 2 == 0:
            return True
        else:
            return False
   
 
x = Number(int(input()))
print(x.isEven)


# 82: Code project - Create a Juice class with name and capacity properties with the ability to add the juices
class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')


    def __add__(self, other):
        self.name = self.name + "&" + other.name
        self.capacity = self.capacity + other.capacity
        return (self.name + ' ('+str(self.capacity)+'L)')


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)
