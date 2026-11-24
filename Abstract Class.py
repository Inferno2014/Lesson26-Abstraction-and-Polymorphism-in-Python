from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        pass
class Bike(Vehicle):
    def wheels(self):
        print('Bikes are Two-Wheelers!')
class Auto(Vehicle):
    def wheels(self):
        print('Autos are Three-Wheelers!')
class Car(Vehicle):
    def wheels(self):
        print('Cars are Four-Wheelers!')
b = Bike()
a = Auto()
c = Car()
b.wheels()
a.wheels()
c.wheels()