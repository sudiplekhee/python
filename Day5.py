name=input("Enter your name:")
print(len(name))
result=len(name)
final=name.rfind("e") # r means reverse from opposite side it will count the letter
name=name.capitalize() #First letter capital banaucha
name=name.upper() #Sabai letter capital banaucha
name=name.lower() #Sabai letter lower banaucha
name=name.isdigit() #It returns either true or false  #Number halim vane matra true return garcha
result=name.isalpha() #Yesma chai space hunu vyena space vyo vane false return garcha 
print(result)
phone_number=input("Enter your mobile number:")
result=phone_number.count("-") #count ley kati ota letter use vako cha vancha number count gardincha kati choty repeat vako number    #How many character are in string
result=phone_number.replace("-","7")  #Replace through kunai pani number remove garera arko halnu painxa
print(result)

print(help(str))



#Validate user input exercise
#1. username is no more than 12 characters
#2.username must not contain spaces
#3.Username must not contain digits


username=input("Enter your username:")
if len(username)>12:
    print("Your usrname cant be more than 12 charcters")
elif not username.find(" ")==-1:
 print("Your username cant contain spaces")
elif not username.isalpha():
 print("Your username cant contain numbers")
else:
    print(f"Welcome{username}")    