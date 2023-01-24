# OOP

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
