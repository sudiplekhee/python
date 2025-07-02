#Typecasting = the process of converting a variable from one data type to another str(),int(),float(),bool()

name="sudip lekhee"
age=21
gpa=3.87
is_student=True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))#when we put type then its shows which datatypes are they

age=float(age)
print(age)
gpa=int(gpa)
print(gpa) #It changes the datatypes like int to string and float to integer

name="sudip"

name=bool(name)
print(name)

age=20
age=str(age)
print(age)


#input()=A function that prompts the user to enter data returns the entered data as a string

name=input("What is your name:")
age=input("Enter your age:")
age=int(input("Enter your age:"))
age=int(age)
age=age+1
print(f"Helllo {name}")
print("HAPPY BIRTHDAY LEKHEE")
print(f"You are {age} years old")


