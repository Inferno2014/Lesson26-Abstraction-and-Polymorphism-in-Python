#This is polymorphism without inheritance
#Python doesn't require a common parent class here. It simply expects the object to support the operation being called.
#This is called duck-typing
class Dog():
    def speak(self):
        print('Dog says Woof!')
class Human():
    def speak(self):
        print('Human says Hello!')
class Robot():
    def speak(self):
        print('Robot says Beep Boop!')
def make_it_speak(obj):
    obj.speak()
d = Dog()
r = Robot()
h = Human()
make_it_speak(d)
make_it_speak(r)
make_it_speak(h)