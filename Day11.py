#Polymorphism = Greek word that means to "have many forms or faces"
#Poly=Many
#morphe=form

#Two ways to achieve polymorphism
#1.Inheritance=An object could be treated of the same type of a parent class
#"Duck typing" Object must have neccesaary attributes/methods
# from abc import ABC, abstractmethod
# class Shape:
#     #Abstract method
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14 *self.radius **2
# class Square(Shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side ** 2
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
#     def area(self):
#         return self.base * self.height *0.5
# class Pizza(Circle):
#     def __init__(self,topping,radius):
#         super().__init__(radius)
#         self.topping=topping

# shapes=[Circle(4),Square(5),Triangle(7,6),Pizza("sudip",16)]
# for shape in shapes:
#     print(shape.area())
    
# #Duck typing"= Another way to achieve polymorphism besides inheritance
# #object must have the minimum necassary attributes/methods
# #"If it looks a duck and quicks like a duck, it must be a duck"

# class Animal:
#     alive=True
    
# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("WOw!")

# class Car:
#     alive=False
#     def speak(self):
#         print("Hahaha hehehe hiw")
# animals=[Dog(),Cat(),Car()]
# for animal in animals:
#     animal.speak()
#     print( animal.alive)
    
#Static method = A method that belong to a class rather than any object from that class(instance)usually sued for genral utility functions

#instance methods=Best for operations on instances of the class(Objects)
#Static method= Best for utility functions that do not need access to class data

# class Employee:
#     def __init__(self,name,position):
#         self.name=name
#         self.position=position
#     def get_info(self):
#         return f"{self.name}={self.position}"
  

#     @staticmethod
#     def is_valid_position(position):
#         valid_positions=["Manager","cashier","Cook","janitor"]
#         return position in valid_positions
# print(Employee.is_valid_position("Cook"))
# employee1=Employee("Sudip","Manager")
# employee2=Employee("Nikhil","cashier")
# employee3=Employee("nishanta","worker") 
# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())

# #class methods= Allow operations related to the class itself
# #Take(s) as the first parameter ,which represents the class itself

# class Student:
#     count=0
#     total_gpa=0
#     def __init__(self,name,gpa):
#         self.name=name
#         self.gpa=gpa
#         Student.count += 1
#         Student.total_gpa += gpa
#         #Instance method
#     def get_info(self):
#         return "{self.name} {self.gpa}"
#     @classmethod
#     def get_count(cls):
#         return f"Total # of students :{cls.count}"
#     @classmethod
#     def average_gpa(cls):
#         if cls.count ==0:
#             return 0
#         else:
#             return f"{cls.total_gpa} {cls.count:.2f}"
# student1=Student("Sudip",3.66)
# student2=Student("Nikhil",3.78)   
# print(Student.get_count())
# print(Student.average_gpa())

#Magic method=Dunder Methods (double underscore) __init__, __str__, __eq__
#They are automatically called by many python's build in operations
#They allow developer to define or customize the behaviour of object


class Book:
    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"   # removed the extra '

    def __eq__(self,other):
        return self.title==other.title and self.author==other.author  # fixed
    def __lt__(self,other): #lt full name is less than
        return self.num_pages < other.num_pages
    def __gt__(self,other): #gt full name is lgreater than
        return self.num_pages > other.num_pages
    def __add__(self,other):
        return self.num_pages+other.num_pages
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self,key):
        if key=="title":
            return self.title 
        elif key=="author":
            return self.author
        elif key=="num_pages":
            return self.num_pages
        else:
            return f"key {key} was not found"
book1=Book("The habbit","sudip",310)
book2=Book("The habbit","sudip",223)
book3=Book("The lion","lekhee cs",172)

# print(book1)          # The habbit by sudip
# print(book1==book2)   # True
print("The lion" in book3)
print(book1["audio"])

# @property=Decorator used to define a method as a property (it can be accessed like an attributes )
#benefits:Add additional logic when read ,write delete attributes 
#gives your better setter and deleter method

class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    @property
    def width(self):
        pass
    @property
    def height(self):
        pass
rectangle=Rectangle(4,5)
print(rectangle._height)
print(rectangle._width)