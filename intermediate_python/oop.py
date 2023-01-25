# Object Orientated Programming 

# 20.2: Create a player class with name and level attributes, as well as an intro method.
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

player_1 = Player(input(), input())
player_1.intro()

# 21.2: Create a Shape base class and a rectangle sub class and with area and perimeter methods respectively.
class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width*self.height)

class Rectangle(Shape):
    def perimeter(self):
        print(self.width * 2 + self.height * 2)
    

w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()

# 22.2: Create a Shape class with the ability to add the widths and heights of shapes, as well as determine if one shape's area is greater than another.
class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width*self.height

    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)
    
    def __gt__(self, other):
        return self.area() > other.area()

w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)

# 23.2: Create a player class with a name and private lives attributes, as well as a hit method which decreases lives by 1.
class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
        if self._lives == 0:
            print("Game Over")
    

p = Player("Cyberpunk77", 3)
p.hit()
p.hit()
p.hit()

# 24.2: Create a Shape class with a static area method
class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    @staticmethod
    def area(w, h):
        return w * h


w = int(input())
h = int(input())

print(Shape.area(w, h))



# 25.2: Add an isAlive property to thee game from 23.2
class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
    
    @property
    def isAlive(self):
        if self._lives > 0:
            return True
    

p = Player("Cyberpunk77", int(input()))
i = 1
while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break

# 27: Code Project - Create a shooting game where lasers work on aliens and guns work on monsters.
class Enemy:
  name = ""
  lives = 0
  def __init__(self, name, lives):
    self.name = name
    self.lives = lives

  def hit(self):
    self.lives -= 1
    if self.lives <= 0:
       print(self.name + ' killed')
    else:
        print(self.name + ' has '+ str(self.lives) + ' lives')

class Monster(Enemy):
  def __init__(self):
    super().__init__('Monster', 3)

class Alien(Enemy):
  def __init__(self):
    super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
    x = input()
    if x == 'exit':
        break
    elif x == "laser":
        a.hit()
    elif x == "gun":
        m.hit()
    