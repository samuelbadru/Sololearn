# Collection Types

# 2.2: Write a program that stores car data and outputs requested information
car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

query = input()

print(car[query])

# 3.2: Write a program that stores the economic freedom rank by country and outputs requested information, with a default value if the country isn't stored.
data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

query = input()

print(data.get(query, "Not found"))

# 4.2: Create a contact list that stores the name and age of each contact and outputs their age when name is searched.
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

query = input()
status = "Not Found"
position = 0


for x in contacts:
    if x[0] == query:
        status = "Found"
        break
    else:
        position += 1
            
if status == "Found":
    print(query + " is " + str(contacts[position][1]))
else:
    print(status)

# 5.2: Make a function that takes the side length of a square as its argument and return the perimeter and area using a tuple.
def calc(x):
    p = x * 4
    a = x * x
    return p, a
    

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))

# 6.2: Output the matched skills between the candidate and job requirements
skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

print(skills & job_skills)

# 7.2: Given a word as input, output a list, containing only the letters of the word that are not vowels.
word = input()

print([i for i in word if i not in ('a', 'e', 'i', 'o', 'u')])

# 10: Code Project - Given a string as input, output how many times each letter appears in the string.
text = input()
dict = {}

for x in text:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

print(dict)
