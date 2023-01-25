# Functional Programming

# 12.2: Create a percentage calculator
price = int(input())
perc = int(input())

res = (lambda x, y : x * y/100)(price, perc)

print(res)

# 13.2: Increase salaries by bonus amount
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())

salaries = list(map(lambda x : x + bonus, salaries))

print(salaries)

# 14.2: Create a generator function that will output prime numbers in a given range.
def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    for x in range(a, b):
        if isPrime(x):
            yield x
    
f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))

# 15.2: Create an invoicing system
def decor(func):
    def wrap(num):
        print("***")
        func(num)
        print("***")
        print("END OF PAGE")
    return wrap

@decor
def invoice(num):
    print("INVOICE #" + num)

invoice(input())

# 16.2: Convert decimal into binary
def convert(num):
   if num == 0:
      return 0 
   return (num % 2 + 10 * convert(num // 2)) 


print(convert(int(input())))

# 17.2: Create a function that returns the minimum value of any given number of inputs 
def my_min(*x):
    return min(x)

print(my_min(8, 13, 4, 42, 120, 7))

# 19: Code Project - Given a string as input, output each letter in reverse order on a new line.
def spell(txt):
    if len(txt) == 1:
        print(txt)
    else:
        spell(txt[1:])
        print(txt[:1])


txt = input()
spell(txt)
