import math
x=10.1
print(math.pi)
print(math.e)
result=math.sqrt(x)
result=math.ceil(x)  #1o vayo vane 11 huncha
result=math.floor(x) #10 vayo vane 1 ley descrese huncha
print(result)


import math

radius=float(input("Enter the radius of a circle:"))

circumference= 2 * math.pi * radius
print(f"The circumference is :{round(circumference,3)}cm") #round halyo vane jasto 2.33544356346 hudaina 2.33 matra  print huncha ani 3 haleko cha ni tele digit paxadi ko kati ota number print garne vaneko ho 2 halim bhane suppose 2.33    3 halim vane 2.333

import math
radius=float(input("Enter Area of circle:"))
area=math.pi * pow(radius, 2)
# print(f"The area of circle is:{round(  area,2)}")

import math

a=float(input("Enter side A:"))
b=float(input("Enter side b:"))

c=math.sqrt(pow(a,2)+pow(b,2))

print(f"Side c={c}")

# 2082/03 /19 written code by lekhi
# if=Do some code only if some condition is True
# Else do something else


age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote")
num=int(input("Enter even or odd number:"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

response=(input("Would you like food? (Y/N):"))
if response=="Y":
    print("Have soome food")
else:
    print("No food for you!")
    
    
name=input("Enter your namr:")
if name=="":
    print("You did not type in your name ")   
else:
    print(f"Hello{name}")
for_sale= True
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")