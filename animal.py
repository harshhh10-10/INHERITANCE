from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("I can walk")

class snake(animal):
    def move(self):
        print("I can crawl")

obj1=human()
obj1.move()
obj2=snake()
obj2.move()