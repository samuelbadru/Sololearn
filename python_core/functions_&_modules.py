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
