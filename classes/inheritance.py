# Programming Concept:
# 'D', 'R', 'Y'
# Don't Repeat Yourself

# class Dog:
#     def walk(self):
#         print('Walk')

# class Cat:
#     def walk(self):
#         print('Walk')

# Repeating the code, not a good practice.. 

class Animal:
    def walk(self):
        print('Walk..')

class Dog(Animal):
    pass

class Cat(Animal):
    def mewo(self):
        print('Mewo..')

d1=Dog()
d1.walk()
c1=Cat()
c1.walk()
c1.mewo()

# pass just mean to pass the line line of code, not to leave the body empty..