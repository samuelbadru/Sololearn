# Dictionaries, Tuples, Sets

# 15.2: Make a contact list and implement search for their email address
contacts = {
    "David": ["123-321-88", "david@test.com"],
    "James": ["241-879-093", "james@test.com"],
    "Bob": ["987-004-322", "bob@test.com"],
    "Amy": ["340-999-213", "a@test.com"]
}

name = input()

if name in contacts:
    print(contacts[name][1])
else:
    print("Not found")

# 17.2: The map is stored as a list of points, calculate and output the distance to the closest point from the point (0, 0).
import math

points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]

distances = []

for (x, y) in points:
    distances.append(math.sqrt(x**2 + y**2))

print(min(distances))



# 18.2: Given two sentences find and output the number of words that are present in both sentences.
s1 = input()
s2 = input()

print(len(set(s1.split()) & set(s2.split())))


# 20.1: Code project - calculate the percentage revenue growth if the ticket discount age changed to the given input. (Adults - $20, under 18s $5)
data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
age = int(input())

cur_rev = 0
for x in data.values():
    if x < 18:
        cur_rev += 5
    else:
        cur_rev += 20


new_rev = 0
for y in data.values():
    if y < age:
        new_rev += 5
    else:
        new_rev += 20

print(int(((new_rev - cur_rev) / cur_rev) * 100))