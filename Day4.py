# Python calculator

operator=input("Enter an operator(+ - * /):")
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

if operator=="+":
    result=num1+num2
    print(round(result,2))
elif operator=="-":
    result=num1-num2
    print(round(result,2))
elif operator=="*":
    result=num1*num2
    print(round(result,2))
elif operator=="/":
    result=num1/num2
    print(round(result,2))     
else:
    print("Wrong operator")    
    
# Python weight converter

weight=float(input("Enter your weight:"))    
unit=input("Kilograms or Pounds ? (K or L):")

if unit=="K":
    weight=weight*2.205
    unit="Lbs."
    print(f"Your weight is :{round(weight,1)}{unit}")  
elif unit=="L":
    weight=weight/2.205  
    unit="kgs." 
    print(f"Your weight is :{round(weight,1)}{unit}")  
else:
 print(f"{unit}was not valid")

# Practice

weight=float(input("Enter your weight:"))
unit=input("Kilograms or pounds ?(K or L):")

if unit=="K":
    weight=weight*2.205
    unit="kgs."
    print(f"The weight is {round(weight,2)} {unit}")
elif unit=="L":
    weight=weight * 2.205
    unit="lbs."
    print(f"The weight is {round(weight,2)} {unit}")
else:
    print("Not validated")

unit=input("Is this temperature in Celsius or Fahrenheit(F/C):")    
temp=float(input("Enter the temperature:"))

if unit=="F":
    temp=round((9 * temp)/5+32,1)
    print(f"The temperature in fahrenheit is {temp}f")
elif unit=="C":
    temp=round((temp-32) * 5/9,1)
    print(f"The temperature in Celsius is {temp}C")
else:
    print("It is inavlid unit of mraesurement")            
    

    
    

