# Working with files

# 35.2: Create a program that outputs a given number of characters of a file.
file = open("/usercode/files/books.txt")
print(file.read(int(input())))
file.close()

# 36.2: Write a program to fill the text file with given number input.
n = int(input())

file = open("numbers.txt", "w+")

for x in range(1, n + 1):
    file.write("\n" + str(x))

file.close()

f = open("numbers.txt", "r")
print(f.read())
f.close()


# 37.2: Create a program which will output how many words each title of a book contains, in the provided format.
with open("/usercode/files/books.txt") as f:
   count = 1
   for line in f:
      num = len(line.split())
      print("Line " + str(count) + ": " + str(num) + " words")
      count += 1


# 39: Code Project - You are given a file named "books.txt" with book titles, each on a separate line. Encode each title with the first letters of each word combined.
file = open("/usercode/files/books.txt", "r")

with file as f:
    code = ""
    for line in f:
        words = line.split()
        for word in words:
            code += word[0]
    print(code)


file.close()
