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
