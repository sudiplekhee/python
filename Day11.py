#Polymorphism = Greek word that means to "have many forms or faces"
#Poly=Many
#morphe=form

#Two ways to achieve polymorphism
#1.Inheritance=An object could be treated of the same type of a parent class
#"Duck typing" Object must have neccesaary attributes/methods
from abc import ABC, abstractmethod
class Shape:
    #Abstract method
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 *self.radius **2
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side ** 2
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return self.base * self.height *0.5
class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping=topping

shapes=[Circle(4),Square(5),Triangle(7,6),Pizza("sudip",16)]
for shape in shapes:
    print(shape.area())
    
#Duck typing"= Another way to achieve polymorphism besides inheritance
#object must have the minimum necassary attributes/methods
#"If it looks a duck and quicks like a duck, it must be a duck"

class Animal:
    alive=True
    
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("WOw!")

class Car:
    alive=False
    def speak(self):
        print("Hahaha hehehe hiw")
animals=[Dog(),Cat(),Car()]
for animal in animals:
    animal.speak()
    print( animal.alive)
    
#Static method = A method that belong to a class rather than any object from that class(instance)usually sued for genral utility functions

#instance methods=Best for operations on instances of the class(Objects)
#Static method= Best for utility functions that do not need access to class datagi