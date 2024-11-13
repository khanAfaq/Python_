class Point:
    def move(self):
        print('Move')

    def draw(self):
        print('Draw')
    
# object of the class or instance of the class
Point1=Point()

# Methods
Point1.move()
Point1.draw()

# Instance
Point1.x=10
Point1.y=20

print(Point1.x)
print(Point1.y)