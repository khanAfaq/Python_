# Constructor is a function it called which at the time of creating the object.

class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    def move(self):
        print('Move')
    def draw(self):
        print('Draw')
    
point=Point(10,20)
print(point.x,point.y)
