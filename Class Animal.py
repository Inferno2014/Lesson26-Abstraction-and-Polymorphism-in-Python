from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Dog(Animal):
    def move(self):
        print('Dogs can walk and run!')
class Snake(Animal):
    def move(self):
        print('Snakes can slither on the ground!')
d = Dog()
s = Snake()
d.move()
s.move()