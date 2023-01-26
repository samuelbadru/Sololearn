# Exceptions

# 29.2: Create a program for an ATM that only takes a number as input
def withdraw(amount):
   print(str(amount) + " withdrawn!")

try:
   withdraw(int(input()))
except ValueError:
   print("Please enter a number")


# 30.2: Create a digital menu and handle cases where input isn't valid.
menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

try:
    print(menu[int(input())])
except (ValueError, IndexError):
    print("Item not found")
else:
    print("Thanks for your order")


# 31.2: Create a program to post tweets, with a max character length of 42
tweet = input()

try:
    if len(tweet) > 42:
        raise ValueError("Max tweet length of 42 characters")
except:
    print("Error")
else:
    print("Posted")


# 33: Code Project - Make a registration form that requires a name of no more than 3 characters.
try:
    name = input()
    if len(name) < 4:
        raise ValueError("Name must be 4 characters or more")
    
except:
    print("Invalid Name")

else:
    print("Account Created")
