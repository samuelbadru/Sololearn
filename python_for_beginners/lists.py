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
