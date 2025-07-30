# # import random
# # import string

# # chars=string.punctuation + string.digits + string.ascii_letters  # yo line ley special charcter haru banaucha encrypted form ma banaucha
# # chars=list(chars) #single single letter banayera print garcha
# # key=chars.copy()
# # random.shuffle(key)
# # print(chars)  
# # print(f"chars:{chars}")
# # print(f"keys:{key}")

# # #ENCRYPT
# # plain_text=input("Enter an message to encrypt:")
# # cipher_text=""

# # for letter in plain_text:
# #     index=chars.index(letter)
# #     cipher_text += key[index]
    
# # print(f"Original message:{plain_text}")
# # print(f"encrypted message:{cipher_text}")

# # #Decrypt

# # cipher_text=input("Enter a message to encrypt:")
# # plain_text=""

# # for letter in cipher_text:
# #     index=key.index(letter)
# #     plain_text +=chars[index]
# # print(f"encrypted message:{cipher_text}") 
# # print(f"Original message:{plain_text}")

# #Hangman in python

# import random
# words=("mango","apple","banana","graphs","pineapple")


# #dictionary of key:()
# hagman_art={0: ("  ",
#                 "  ",
#                 "  "),
#             1: (" o ",
#                 "  ",
#                 "  "), 
#             2: (" o ",
#                 " | ",
#                 "   "), 
#             3: (" o ",
#                 " /| ",
#                 "   "), 
#             4: (" o ",
#                 " \|/ ",
#                 "  "), 
#             5:(" o ",
#                 " \|/ ",
#                 " / "),
#             6: (" o ",
#                 " \|/ ",
#                 " /\\ ")
# }
# def display_name(wrong_guesses):
#     for line in hagman_art[wrong_guesses]:
#         print(line)

# def display_hint(hint):
#     pass
# def display_answer(answer):
#     pass
# def main():
#     answer=random.choice(words)
#     print(answer)
#     hint=["_"] * len(answer)
#     print(hint)
#     wrong_guesses=0
#     guessed_letters=set()
#     is_running= True
    
#     while is_running:
#         display_name(wrong_guesses)
#         display_hint(hint)
#         guess=input("Enter a letter:").lower()

# if __name__ == "__main__":
#     main()
                
#object=A "bundle" of related attributes (variables) and methods (functions) 
#example is phone,cup,book
#You need a "class" to create many objects


#class=(blueprint)used to design the structure and layout of an object 
      
# class Car:
#     # def __init__(self): #we need this method(function) to create an object
#     def __init__(self,model,year,color,for_sale):
#         self.model=model
#         self.year=year
#         self.color=color
#         self.for_sale=for_sale
    # car1 #This is object now
from car import Car  #capital Car is class
car1=Car("Mustang","2025","red",False)       
car2=Car("lamborgini","white","2026",True)
car3=Car("lamborgini","white","2026",True)


# every_car=[car1,car2]
# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)
car1.drive()
car2.stop()
car3.describe()

#class variables= shared among all instances of a class
#Defined outside the constructor
#Allow you to share data among all objects created from that class

class Student:
    class_year=2026
    num_students=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.num_students += 1
student1=Student("sudip",21)
student2=Student("Nikhil",20)
student2=Student("Nikhil",20)
print(student1.name)
print(student1.age)
print(Student.class_year) #Direct class name bata in print garna sakincha

print(Student.num_students)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students") #Class ko through pani call garna milyo haii self nai chayincha vanera chaina


#Inheritance= Allows a class to inherit attributes and methods from another class 
#Helps with code reusability and extensibility
#class child(Parent)