# # Python calculator

# operator=input("Enter an operator(+ - * /):")
# num1=float(input("Enter the first number:"))
# num2=float(input("Enter the second number:"))

# if operator=="+":
#     result=num1+num2
#     print(round(result,2))
# elif operator=="-":
#     result=num1-num2
#     print(round(result,2))
# elif operator=="*":
#     result=num1*num2
#     print(round(result,2))
# elif operator=="/":
#     result=num1/num2
#     print(round(result,2))     
# else:
#     print("Wrong operator")    
    
# # Python weight converter

# weight=float(input("Enter your weight:"))    
# unit=input("Kilograms or Pounds ? (K or L):")

# if unit=="K":
#     weight=weight*2.205
#     unit="Lbs."
#     print(f"Your weight is :{round(weight,1)}{unit}")  
# elif unit=="L":
#     weight=weight/2.205  
#     unit="kgs." 
#     print(f"Your weight is :{round(weight,1)}{unit}")  
# else:
#  print(f"{unit}was not valid")

# # Practice

# weight=float(input("Enter your weight:"))
# unit=input("Kilograms or pounds ?(K or L):")

# if unit=="K":
#     weight=weight*2.205
#     unit="kgs."
#     print(f"The weight is {round(weight,2)} {unit}")
# elif unit=="L":
#     weight=weight * 2.205
#     unit="lbs."
#     print(f"The weight is {round(weight,2)} {unit}")
# else:
#     print("Not validated")

# unit=input("Is this temperature in Celsius or Fahrenheit(F/C):")    
# temp=float(input("Enter the temperature:"))

# if unit=="F":
#     temp=round((9 * temp)/5+32,1)
#     print(f"The temperature in fahrenheit is {temp}f")
# elif unit=="C":
#     temp=round((temp-32) * 5/9,1)
#     print(f"The temperature in Celsius is {temp}C")
# else:
#     print("It is inavlid unit of mraesurement")


#Logical operator=Evaluate multiple condition(or,and,not)
#or=at least one condition must be true
#and=both conditions must be true
#not=inverts the condition(not false,not true)

# temp=67
# is_raining=True

# if temp>45 or temp<0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")        
    
    
# temp=28
# is_sunny=True
# if temp>=28 and is_sunny:
#     print("It is hot outside") 
#     print("It is sunny")     
    
# elif temp <=0 and is_sunny:
#     print("It is cold outside") 
#     print("It is sunny") 

    
# elif 28> temp> 0 and is_sunny:
#     print("It is warm outside") 
#     print("It is sunny") 
    
# elif 28> temp> 0 and not is_sunny:
#     print("It is cold outside") 
#     print("It is sunny") 
    
# elif 28> temp> 0 and  not is_sunny:
#     print("It is cold outside") 
#     print("It is sunny")          

# elif 28> temp> 0 and not is_sunny:
#     print("It is cold outside") 
#     print("It is sunny")     


#Conditional Expression= A one-line shortcut for the if_else statement(ternary operator)
#print or assign one of two values based on a condition
#if condition else Y 

num=-5
print("Positive" if num>0 else "Negative")

num=1
print("Even number" if num%2==0 else "odd number")

a=10
b=5
age=25
temp=10
max_num=a if a>b else b
min_num=a if a<b else b
print(max_num)
print(min_num)

status="Adult" if age>=18  else "Child"
print(status)

weather="Hot" if temp>20 else "Cold"
print(weather)


control="admin"
ok="Full Access"if control=="admin" else "Limited Access"
print(ok)
    

