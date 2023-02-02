# Lists

# 9.2: Create a program that will take an eye color as input and output the percentage of people with that eye color in the room.
data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]
color = input()

total = 0

for x in data:
    total += sum(x)

if color == 'brown':
  print(int(((data[0][0] + data[1][0]) / total) * 100))
elif color == 'blue':
  print(int(((data[0][1] + data[1][1]) / total) * 100))
elif color == 'green':
  print(int(((data[0][2] + data[1][2]) / total) * 100))
elif color == 'black':
  print(int(((data[0][3] + data[1][3]) / total) * 100))


# 10.2:Calculate and output the number of houses that have a price that is above the average.
prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]

average = sum(prices) / len(prices)

count = 0

for x in prices:
    if x > average:
        count += 1

print(count)

# 11.2: Create a list which will contain 12 items, each showing the number of insects doubled in size at the beginning of that month. 
n = int(input())

print([n * 2 ** m for m in range(12)])


# 13: Code Project - Create an average word length calculator
text = input()

words = text.split()

total_len = 0

for word in words:
    total_len += len(word)

print(total_len / len(words))