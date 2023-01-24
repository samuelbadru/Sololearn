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
