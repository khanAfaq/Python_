class Person:
    def __init__(self,name) -> None:
        self.name=name

    def profession(self):
        print(f'Hi, {self.name} Computer Engineer.')

p1=Person('Afaq')
print(p1.name)
p1.profession()
