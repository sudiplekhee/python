# import random

# # options=("rock","paper","scissors")
# # player= None
# # computer=random.choice(options)
# # player=input("Enter a choice (rock,paper,scissors):")
# # print(f"Player:{player}")
# # print(f"Computer:{computer}")

# options=("rock","paper","knife")
# player= None
# computer=random.choice(options)
# running=True
# player=input("Enter a choice(rock,paper,knife):")
# print(f"player:{player}")
# print(f"computer:{computer}")

# if player==computer:
#     print("It's a tie!")
# elif player=="rock" and computer=="scissors":
#     print("You win!")
# elif player=="paper" and computer=="rock":
#     print("you win!")
# elif player== "scissors" and computer=="paper":
#     print("You win?!")
# else:
#     print("You lose!")


# import random
# # ● ┌ ┐ │ └ ┘
# "┌---------┐ "
# "│         │"
# "│         │"
# "│         │"
# "└---------┘"

# dice_art={
#     1:("┌---------┐",  #These all are key values pair
#        "│         │",
#        "│    #    │",
#        "│         │",
#        "└---------┘"),
#     2:("┌---------┐",  #These all are key values pair
#        "│   #     │",
#        "│         │",
#        "│        ●│",
#        "└---------┘"),
#     3:("┌---------┐",  #These all are key values pair
#        "│  ●      │",
#        "│    ●    │",
#        "│       ● │",
#        "└---------┘"),
#     4:("┌---------┐",  #These all are key values pair
#        "│  ●    ● │",
#        "│         │",
#        "│  ●    ● │",
#        "└---------┘"),
#     5:("┌---------┐",  #These all are key values pair
#        "│  ●    ● │",
#        "│     ●   │",
#        "│  ●    ● │",
#        "└---------┘"),
#  6:   ("┌---------┐",  #These all are key values pair
#        "│ ●  ●  ● │",
#        "│         │",
#        "│ ●  ●  ● │",
#        "└---------┘")
# }
# dice=[]
# total=0
# num_of_dice=int(input("How many dice?:"))
# for die in range(num_of_dice):
#  dice.append(random.randint(1, 6))
# print(dice)

# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#       print(line)
# for line in range(5):
#    for die in dice:
#       print(dice_art.get(die)[line], end="")
#    print()

# for die in dice:
#    total += die
# print(f"Total:{total}")


# #function =A block of reusable code
# place()after the function name to invoke it

# def happy_birthday(name,age):
#    print(f"Happy Bithday {name}")
#    print(f"You are {age} years old")
#    print("Thank you so much")
   
# happy_birthday("sudip","21")
# happy_birthday("nikhil","20")
# happy_birthday("Nishant","22")

# def display_invoice(username,amount,due_date):
#    print(f"Hello {username}")
#    print(f"Your bill of ${amount:.2f} is due :{due_date}")
# display_invoice("Sudip",100.01,"01/02")

# #return=statement used to end a function and send a result back to the caller
# def add(x,y):
#   z=x+y
#   return z
# def substract(x,y):
#    z=x-y
#    return z
# def multiply(x,y):
#    z=x*y
#    return z
# def division(x,y):
#    z=x/y
#    return z

# print(add(1,2))
# print(substract(1,2))
# print(multiply(1,2))
# print(division(1,2))


# def create_name(first,last):
#    first=first.capitalize()
#    last=last.capitalize()
#    return first + " " + last
# full_name=create_name("sudip","chaudhary")
# print(full_name)


# #default arguments=A default value for certain parameters and default is used when that argument is omitted and make your functions more flexible,reduces # o arguments 1.positional 2.Default,3.Keyword,4.arbitary
   
# def net_price(list_price,discount=0,tax=0.05):
#    return list_price * (1-discount) *(1+tax)  #yesko bhitra valuen halda in execute huncha hai ta
# print(net_price(500,0,0.25))    # yesma halyo vane mathy ma haleko value execute hudaina tala ko value matra execute huncha

# import time

# def count(start,end):  #yesma pani value halda huncha default arguments number vANCHA teslai hai 
#    for x in range(start,end+1):  # +1 garyo vane 10 sammai print huncha +1 garena vane 9 samma matra print huncha
#       print(x)
#       time.sleep(1)
#    print("Done boss")
# count(0,10)


# #keyword arguments= An arguments precedded by an identifier helps with readablity order of arguments doesnt matter 1.positional, 2.default 3.keyword 4.arbitary

# def hello(greeting,title,first,last):
#    print(f"{greeting} {title} {first} {last}")
   
# hello("Hello","Mr.","Sudip","Chaudhary")
   
# hello("Hello",first="Sudip",last="Chaudhary",title="Mr.") #ja sukai rakhey pani sequently print huncha


# for x in range(1,11):
#    print(x,end=" ")
   
# print("1","2","3","4","5","6","7",sep="-")  #sep means separate it sepearte the value like i give symbol - then the output will come 1-2-3-4-5-6-7

# def get_phone(country,area,first,last):
#    return f"{country}-{area}-{first}-{last}"
# phone_num=get_phone(country=1,area=12,first=123,last=7789)
# print(phone_num)

# #args=allows you to pass mutiple non-key arguments
# #kwargs=allows you to pass multiple keyword-arguments
# #unpacking operator
# #Today we will discuss about arbitary operator

# def add(*args):   #parathesis bhitra *args pass garim vane add(1,2,3,4,5) jati pani halnu milxa add garnu milcha
#    total=0
#    for arg in args:
#       total += arg
#    return total
# print(add(1,2,3,4))

# def display_name(*args):
#    for arg in args:
#       print(arg, end=" ")
# display_name("sudip","lekhee","hehe","jaja","lala")  #args pass garim vane jati pani value pass garnu milxa if hamile *args ko sato a,b pass gareko vaye dui ota value matra halnu milthiyo

# def address(**kwargs):  #**kwargs ma tala gayera lekhda huncha jastai street= but in *args ma "sudip" yesto huncha
#    #for value in kwargs.values():
#    for key, value in kwargs.items(): #items ley sabai print garcha
#       print(f"{key}:{value}")
      
# address(street="123 khanar",
#         city="Itahari",
#         state="MI",
#         zip="2345")

# def shipping_label(*args,**kwargs):
#    for arg in args:
#       print(arg,end=" ")
#       print()
#    # for value in kwargs.values():
#    for key , value in kwargs.items():
      
#       print(f"{key}:{value}")
#       print(f"{kwargs.get('street')}")#tele street matra get garcha euta ma ' lincha haii "" yesto lidaina
# shipping_label("Mr.","Sudip","lekhee",
#                street="Itahari",
#                place="sunsari",
#                haha="how")
   
#Iterable= An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop 
#Note it tuple and list can be reversed but set cannot be reversed

numbers=[1,2,3,4,5,6,7,8]
for number in numbers:
   print(number)
for number in reversed(numbers):
   print(number,end=" ")
   
my_dictionary={"A":"Sudip","B":"Chaudhary"}
for key,value in my_dictionary.items():
   print(key,value)
   
   
#Membership operators=used to test whether a value or variable is found in a sequence(string,list,tupple or dictionary)
#1.in 2.not in

word="sudip"
letter=input("Guess a letter in the secret code:")
if letter in word: #in means to find whether the value is in the word or not
   print(f"The {letter} is found")
else:
   print(f"{letter} not found")

word="sudip"
letter=input("Guess a letter in the secret code:")

if letter not in word: #in means to find whether the value is in the word or not
  print(f"{letter} not found")
else:
  print(f"The {letter} is found")
  
student={"sudip","lekhee","anddic"}
teacher={"bishal","prajwal","prabesh"}
name=input("Enter name:")
if name in student:
   print(f"He is {name} student")
elif name in teacher:
     print(f"He is {name} teacher")
else:
   print("Nobody {name} was found")
   
grades={"sudip":"A",
        "Anddic":"B",
        "Lekhee":"C",
        "HAHA":"D",
        "HEHE":"E"}
student=input("Enter the name of a student:")
if student in grades:
      
   print(f"{student} grade is {grades[student]}") 
   print(f"{student} grade is {grades}")  #grades halim bhane sabai student ko prindt huncha but grades[student] garim vane name lekheko matra print huncha 
else:
   print(f"{student} was not found") 
   
email="sudipchaudhary123gmail.com"

if "@" in email and "." in email:
   print("validate email")
else:
   print("Not validate email")
    
    




