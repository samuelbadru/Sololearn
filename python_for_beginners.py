# Basic concepts

# 3.2: How many seconds are in a month (30 days)?
# Seconds in an hour = 60 * 60, hours in day = 24 days in month = 30
print(30 * 24 * 60 * 60)

# 5.2: A bacteria culture starts with 500 bacteria and doubles in size every hour, calculate the output after 24 hours
# Stating value * 2^number of cycles
print(500 * 2 ** 24)

# 6.2: What's the number of hours and minutes in 888 minutes?
# Hours - floor division is // which gives you the quotient,
print(888 // 60)
# Minutes - modulo operator is % which gives remainders
print(888 % 60)

# 8: Code Project - Calculate the flight time from LA to Sydney, covering a distance of 7425 miles at 550/mph (answer is a float)
print(7425 / 550)



# Strings

# 9.2: Output: "Stay hungry, stay foolish" by Steve Jobs
print('"Stay hungry, stay foolish" by Steve Jobs')

# 10.2: Fix the code to output a triangle of stars that has 4 rows.
print("*\n**\n***\n****")

# 11.2: Create a program to output "hi" 42 times, without any separators, on the same line.
print('hi' * 42)

# 13: Code Project - Make a leaderboard board. The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot.
print("""1.
2.
3.
4.
5.
6.
7.
8.
9.""")



# Variables

# 15.2: Complete the contact management system code to output "name is age years old", where name and age are the declared variable values.
name = "James"
age = "42"
print(name + " is " + age + " years old")

# 16.2: Write a notification program that takes the text as input and outputs it by adding 3 stars at the beginning and the end.
Notification = input()
print("*** " + Notification + " ***")

# 17.2: Change 15.2's code to take the name and age from user input and use them in the output.
name = input()
age = input()
print(name + " is "+age+" years old")

# 20: Code Project - Make a 20% tip calculator that takes the bill amount as input and outputs the tip as a float
bill = int(input())
print((bill * 20) / 100)



# Control Flow

# 22.2: Make a gold purity checker that only accepts 22K (91.7% or more gold) or 24K (99.9% or more)
purity = float(input())
if purity >= 91.7:
 print("Accepted")

# 23.2: Make a program to check if the input year is a leap year or not. 
'''
To check whether a year is a leap year or not, you need to check the following:
1) If the year is evenly divisible by 4, go to step 2. Otherwise, the year is NOT leap year.
2) If the year is evenly divisible by 100, go to step 3. Otherwise, the year is a leap year.
3) If the year is evenly divisible by 400, the year is a leap year. Otherwise, it is not a leap year.
'''
year = int(input())
if year % 4 != 0:
 print("Not a leap year")
elif year % 100 != 0 or year % 400 == 0:
 print("Leap year")
else:
 print("Not a leap year")

# 24.2: Improve gold purity checker from 22.2 by outputting the corresponding purity level
'''
24K - 99.9%
22K - 91.7%
20K - 83.3%
18K - 75.0%
'''
purity = float(input())
if 75 <= purity < 83.3:
 print("18K")
elif 83.3 <= purity < 91.7:
 print("20K")
elif 91.7 <= purity < 99.9:
 print("22K")
elif 99.9 <= purity < 100:
 print("24K")

# 25.2:  Make a game where the player takes 4 shots and can either hit or miss and you output their remaining points.
'''
The player starts with 100 points, with a hit adding 10 points to the player's score, and a miss deducting 20 points.
'''
points = 100
turns = 0

while turns < 4:
 shot = input()
 if shot == "hit":
  points += 10
 elif shot == "miss":
  points -= 20 
 turns += 1

print(points)

# 26.2: Make a ticketing system where you take the ages of 5 passengers and outputs the total price of tickets.
'''
The price of a single ticket is $100.
For children under 3 years old, the ticket is free.
'''
total = 0
passengers = 0

while passengers < 5:
 passengers += 1
 age = int(input())
 if age < 3:
  continue
 else:
  total += 100

print(total)

# 28: Code project - Make a BMI calculator
'''
BMI = weight / height^2
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more
'''
weight = float(input())
height = float(input())
bmi = weight / height ** 2

if bmi < 18.5:
 print("Underweight")
elif 18.5 <= bmi < 25:
 print("Normal")
elif 25 <= bmi < 30:
 print("Overweight")
elif bmi >= 30:
 print("Obesity")



# Lists

# 29.2: Make a ticketing program that takes the seat row and column as input, and outputs the corresponding code from the list.
seats = [
['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', 'i'],
['j', 'k', 'l']
]

row = int(input())
column = int(input())
print(seats[row][column])

# 30.2: Produce someone's initals given their name
fname = input()
lname = input()
print(fname[0] + '.' + lname[0] + '.')

# 31.2: Make a voice recognition system, in which you check if the given command is supported or not.
commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]

x = input()
if x in commands:
 print("OK")
else:
 print("Not supported")

# 32.2: Make a shopping cart program, in which you apply a given discount to the prices in the cart and then output the total cart price.
cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0
for i in cart:
 total += i - (i * (discount / 100))

print(total)

# 33.2: Create a program that takes the total number of floors of a building as input and outputs the floors that have restrooms.
'''
A group of buildings have restrooms on every 5th floor.
For example, a building with 12 floors has restrooms on the 5th and 10th floors.
'''
n = int(input())

for i in range(5, n+1, 5):
 print(i)

# 33.3: Given a string as input, output its reverse.
x = input()
print(x[::-1])

# 36: Code Porject -  Find the sum of the first N numbers.
N = int(input())
sum = 0
for x in range(1, N + 1):
 sum += x
 
print(sum)



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
