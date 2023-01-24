# Pythonicness & Packaging

# 94.2: Make a sum function that takes as many numbers as input
def adder(x, *args):
    answer = x
    for i in args:
        answer += i
    
    print(answer)

adder(2, 3)
adder(2, 3, 4)
adder(1, 2, 3, 4, 5)

# 96.2: Create an ATM system with a minimum withdrawl value of £500
balance = int(input())
to_cash = int(input())

money_left = balance-to_cash if to_cash<=balance and to_cash >= 500 else "Error"

print(money_left)

# 97.2: Create an age checker for a ride with a minimum age of 16
ages = []
i = 0
while i<3:
   age = int(input())
   if age < 16:
      print("Too young!")
      break
   ages.append(age)
   i+=1
   
else:
   print("Get ready!")
   

# 103: Code Project - Write a function that concatenates words, with a dash as a separator
def concatenate(word,*args):
    result = word

    for x in args:
        result = result + "-" + x

    return result
    

print(concatenate("I", "love", "Python", "!"))