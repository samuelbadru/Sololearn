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
