#matchcase statement (switch):An alternative to using 'elif' statements
#Execute some code if a value matches a 'case'
#benefits: cleaner and syntax is more readable

# def day_of_week(day):
#     if day==1:
#         return "It is sunday"
#     elif day==2:
#         return "It is monday"
#     elif day==3:
#         return "It is tuesday"
#     elif day==4:
#         return "It is wednesday"
#     elif day==5:
#         return "It is thursday"
#     elif day==6:
#         return "It is friday"
#     elif day==7:
#         return "It is saturday"
#     else:
#         return "Not valiodate"
# total =day_of_week(2)
# print(total)

# def day_of_week(day):
#  match day:
#     case 1:
#         return "It is sunday"
#     case 2:
#         return "It is monday"
#     case 3:
#         return "It is tuesday"
#     case 4:
#         return "It is wednesday"
#     case 5:
#         return "It is thursday"
#     case 6:
#         return "It is friday"
#     case 7:
#         return "It is saturday"
#     case _:
#         return "Not valiodate"
# total =day_of_week(9)
# print(total)

# def isweekend(Day):
#     match Day:
#         case "Monday":
#             return True
#         case "sunday":
#             return False
#         case "Monday":
#             return False
        
# print(isweekend("Monday"))

# def isweekend(Day):
#     match Day:
#         case "Monday" | "saturday" | "friday":    # | this symbol is known as or operator
#             return True
#         case "sunday":
#             return False
#         case "Monday":
#             return False
        
# print(isweekend("friday"))


#Module= a file containing code you want to include in your program
#use 'import' to include (built-in or your own)
#useful to break up a large program reuable separate files

print(help("modules"))
import math 
import math as m  #math shortcut name
from math import pi
from math import e
print(e)
from math import e
a,b,c,d,e=1,2,3,4,5
print(e ** a)  # **this two star is like a square
print(e ** b)
print(e ** c)
print(e ** d)
print(e ** e)

import math
a,b,c,d,e=1,2,3,4,5
print(math.e ** a)  # **this two star is like a square
print(math.e ** b)  # e lekheko cha ni tesko value e ma import vayera output aako ho
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)


# variable scope=where a varaiable is visible and accesible
# scope resolution =(LEGB) local-->Enclosed --> Global -->Built in

This is local 
def func1():
    a=1  #If we declared variable and values in inside the funxtion it is call as local function
    print(a)  #The function 1 cannot see the function  be inside only the unction a will be showed becuase it was declared
    
def fun2():
    b=2
    print(b)
func1()
fun2()


#This is global

def fun1():
    print(x)
def fun2():
    print(y)
    
x=8
y=6
fun1()
fun2()

#This is built in function

from math import e
def fun1():
  print(e)
e=7
fun1()

#if__name__ ==__main__:(this script can be imported OR run standalone)
#function and classes in this module can be reused 
#without the main block of code executing