# # # import random
# # # import string

# # # chars=string.punctuation + string.digits + string.ascii_letters  # yo line ley special charcter haru banaucha encrypted form ma banaucha
# # # chars=list(chars) #single single letter banayera print garcha
# # # key=chars.copy()
# # # random.shuffle(key)
# # # print(chars)  
# # # print(f"chars:{chars}")
# # # print(f"keys:{key}")

# # # #ENCRYPT
# # # plain_text=input("Enter an message to encrypt:")
# # # cipher_text=""

# # # for letter in plain_text:
# # #     index=chars.index(letter)
# # #     cipher_text += key[index]
    
# # # print(f"Original message:{plain_text}")
# # # print(f"encrypted message:{cipher_text}")

# # # #Decrypt

# # # cipher_text=input("Enter a message to encrypt:")
# # # plain_text=""

# # # for letter in cipher_text:
# # #     index=key.index(letter)
# # #     plain_text +=chars[index]
# # # print(f"encrypted message:{cipher_text}") 
# # # print(f"Original message:{plain_text}")

# # #Hangman in python

# # import random
# # words=("mango","apple","banana","graphs","pineapple")


# # #dictionary of key:()
# # hagman_art={0: ("  ",
# #                 "  ",
# #                 "  "),
# #             1: (" o ",
# #                 "  ",
# #                 "  "), 
# #             2: (" o ",
# #                 " | ",
# #                 "   "), 
# #             3: (" o ",
# #                 " /| ",
# #                 "   "), 
# #             4: (" o ",
# #                 " \|/ ",
# #                 "  "), 
# #             5:(" o ",
# #                 " \|/ ",
# #                 " / "),
# #             6: (" o ",
# #                 " \|/ ",
# #                 " /\\ ")
# # }
# # def display_name(wrong_guesses):
# #     for line in hagman_art[wrong_guesses]:
# #         print(line)

# # def display_hint(hint):
# #     pass
# # def display_answer(answer):
# #     pass
# # def main():
# #     answer=random.choice(words)
# #     print(answer)
# #     hint=["_"] * len(answer)
# #     print(hint)
# #     wrong_guesses=0
# #     guessed_letters=set()
# #     is_running= True
    
# #     while is_running:
# #         display_name(wrong_guesses)
# #         display_hint(hint)
# #         guess=input("Enter a letter:").lower()

# # if __name__ == "__main__":
# #     main()
                
# #object=A "bundle" of related attributes (variables) and methods (functions) 
# #example is phone,cup,book
# #You need a "class" to create many objects


# #class=(blueprint)used to design the structure and layout of an object 
      
# # class Car:
# #     # def __init__(self): #we need this method(function) to create an object
# #     def __init__(self,model,year,color,for_sale):
# #         self.model=model
# #         self.year=year
# #         self.color=color
# #         self.for_sale=for_sale
#     # car1 #This is object now
# from car import Car  #capital Car is class
# car1=Car("Mustang","2025","red",False)       
# car2=Car("lamborgini","white","2026",True)
# car3=Car("lamborgini","white","2026",True)


# # every_car=[car1,car2]
# # print(car1.model)
# # print(car1.year)
# # print(car1.color)
# # print(car1.for_sale)
# car1.drive()
# car2.stop()
# car3.describe()

# #class variables= shared among all instances of a class
# #Defined outside the constructor
# #Allow you to share data among all objects created from that class

# class Student:
#     class_year=2026
#     num_students=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         Student.num_students += 1
# student1=Student("sudip",21)
# student2=Student("Nikhil",20)
# student2=Student("Nikhil",20)
# print(student1.name)
# print(student1.age)
# print(Student.class_year) #Direct class name bata in print garna sakincha

# print(Student.num_students)
# print(f"My graduating class of {Student.class_year} has {Student.num_students} students") #Class ko through pani call garna milyo haii self nai chayincha vanera chaina


# #Inheritance= Allows a class to inherit attributes and methods from another class 
# #Helps with code reusability and extensibility
# #class child(Parent)


class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
Dog=Animal("Cow","black")
print(f"The {Dog.name} is {Dog.color}")

class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class Dog(Animal):
    def speak(self):
        print("WOW DOG")
class Cat(Animal):
    def speak(self):
        print("WOW Cat")
class Mouse(Animal):
    pass

dog= Dog("Sudip",)
cat= Cat("Lekhee")
mouse= Mouse("mickey")
print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()


#multiple inheritance= Inherit from more than one parent class C(A,B)

# Multilevel inheritance=inherit from a parent which inherits from another parent C(B) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"He is {self.name} eating")

    def dance(self):
        print(f"He is {self.name} dancing")
        

class Prey(Animal):
    def flee(self):
        print(f"This animal {self.name} is fleeing")


class Predator(Animal):  # fixed spelling and inheritance
    def hunt(self):
        print(f"This animal {self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


# Example usage:
rabbit1 = Rabbit("Bunny")
rabbit1.dance()   # ✅ Works now
rabbit1.flee()

hawk1 = Hawk("Eagle")
hawk1.hunt()

fish1 = Fish("Nemo")
fish1.flee()
fish1.hunt()

#super()=function used in a child class to call methods from a parent class(superclass).
#Allow you to extend the functionality of the inherited methods

class Shape:
      def __init__(self,color,isfilled):
        self.color=color
        self.isfilled=isfilled
      def describe(self):
          print(f"it is {self.color} and {'filled' if self.isfilled else 'not filled'}")
class Circle(Shape):
    def __init__(self,color,isfilled,radius):
        super().__init__(color,isfilled)
        self.radius=radius
    def describe(self):
        print(f"It is circle with an area of {3.14*self.radius*self.radius}") #this lines of code will work the upper parent class will not work if in circle the describe mathod is not done then parent class will worked
        super().describe() #It is imported from the parent upper class
class Square(Shape):
     def __init__(self,color,isfilled,width):
        super().__init__(color,isfilled)
        self.width=width
     def describe(self):
        print(f"It is square with an area of {self.width*self.width}cm^2") #this lines of code will work the upper parent class will not work if in circle the describe mathod is not done then parent class will worked
        super().describe()
class Triangle(Shape):
    def __init__(self,color,isfilled,width,height):
        super().__init__(color,isfilled)
        self.width=width
        self.height=height
    def describe(self):
        print(f"It is traingle with an area of {self.width*self.height}cm^2") #this lines of code will work the upper parent class will not work if in circle the describe mathod is not done then parent class will worked
        super().describe()
    
        
circle=Circle(color="red",isfilled=True,radius=6)
square=Square(color="blue",isfilled=True,width=6)
triangle=Triangle(color="blue",isfilled=True,width=6,height=10)
print(circle.color)
print(circle.isfilled)
print(circle.radius)
print(square.color)
print(square.isfilled)
print(square.width)   
print(triangle.color)
print(triangle.isfilled)
print(triangle.width)  
print(triangle.height)  
circle.describe()
square.describe()
triangle.describe()
