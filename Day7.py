#Shopping card program

# foods=[]
# prices=[]
# total=0
# while True:
#     food=input("Enter a food to buy(q to quit):")
#     if food.lower()=="q":  # lower halim nita capital Q pani support garcha
#         break
#     else:
#         price=float(input(f"Enter the price of a {food}:$"))
#         foods.append(food)
#         prices.append(price)
# for food in foods:
#     print(food,end=" ")
    
# for price in prices:
#     total += price
#     print()
#     print(f"Yout Total is :${total}")


# # Toady we will describe about 2D list
# fruits=    ["apple","banana","orange","mango"]
# vegetables=["ce4lery","carrots","potatoes"]
# meats=     ["chicken","fish","turkey"]

# groceries=[fruits,vegetables,meats]

# # print(groceries[0])

# print(groceries[0][1]) #row zero column one

# groceries=[  ["apple","banana","orange","mango"],["celery","carrots","potatoes"],["chicken","fish","turkey"]]

# for collection in groceries:
#     for food in collection:  #we use nested loop 
#      print(food,end=" ")
#     print()     #We use print() for arrangi8ng in proper in way 

# num_pad=((1,2,3),
#          (4,5,6),
#          (7,8,9),
#          ("*",0,"#"))
# for row in num_pad:
#     for everyrow in row:
#      print(everyrow,end=" ")
#     print()


#Python Quiz game


# questions = (
#     "How many elements in periodic table?:",
#     "Which animal lays the largest eggs?:",
#     "What is the most abundant gas in Earth's atmosphere?:",
#     "How many bones are in the human body?:",
#     "Which planet in the solar system is the hottest?:"
# )

# options = (
#     ("A.116", "B.117", "C.118", "D.119"),
#     ("A.Whale", "B.Crocodile", "C.Elephant", "D.Ostrich"),
#     ("A.Nitrogen", "B.Oxygen", "C.Carbon-dioxide", "D.Hydrogen"),
#     ("A.206", "B.207", "C.208", "D.209"),
#     ("A.Mercury", "B.Venus", "C.Earth", "D.Jupiter")
# )

# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("\n------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)
    
#     guess = input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)

#     if guess == answers[question_num]:
#         score += 1
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{answers[question_num]} is the correct answer.")
    
#     question_num += 1

# # Final Score
# print("\n==================")
# print("      RESULT      ")
# print("==================")
# print("Correct Answers:", answers)
# print("Your Guesses:   ", guesses)
# print(f"Your Score: {score}/{len(questions)}")



#dictionary = a collection of {key:value}pairs
#ordered and changeable. No duplicates


capitals={"USA":"Washington D.C.",
          "Nepal":"Kathmandu",
          "India":"New Delhi",
          "China":"Beijing"}
print(dir(capitals))
print(help(capitals))
print(capitals.get("USA"))
print(capitals.get("Nepal"))
print(capitals.get("India"))
print(capitals.get("China"))
print(capitals.get("Japan"))

if capitals.get("China"):
    print("That capital city is matched")
else:
#     print("That capital doesnt exist")  

capitals.update({"USA":"Berlin"})
print(capitals)
capitals.pop("Nepal") #pop vaneko remove garcha
print(capitals)
capitals.popitem() #dont need to add any value 
capitals.clear() #clear all the dictionary
print(capitals)
keys=capitals.keys() #Sabailai list ma banai dincha like that dict_keys(['USA', 'Nepal', 'India', 'China'])
for key in capitals.keys(): #USA
# Nepal
# India
# China  yesari print garcha
 print(key)

values=capitals.values()  #dict_values(['Washington D.C.', 'Kathmandu', 'New Delhi', 'Beijing']) yo print garcha key :value   value print garcha 
for value in capitals.values():  #Washington D.C.
# Kathmandu
# New Delhi
# Beijing for loop use garim vane yesto print garcha
 print(value)

items=capitals.items() #dict_items([('USA', 'Washington D.C.'), ('Nepal', 'Kathmandu'), ('India', 'New Delhi'), ('China', 'Beijing')])
print(items)

for key,value in capitals.items():
    print(f"{key}:{value}") #USA:Washington D.C.
Nepal:Kathmandu
India:New Delhi
China:Beijing print garcha yestop loop lagayera garim vane

Concession stand program

dictionary{key:value}

menu={"pizza":3.00,
      "nachos":4.50,
      "popcorn":6.00,
      "fries":2.50,
      "chips":1.00,
      "pretzel":3.50,
      "soda":3.00,
      "lemoade":4.25}
cart=[]
total=0
print("--------MENU--------")
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("--------------------")
while True:
    food=input("Select an item (q to quit):")
    if food.lower()=="q":
        break
    elif menu.get(food)is not None:
        cart.append(food)
for food in cart:
    total += menu.get(food)
print(food,end="")
print()
print(f"Total is :${total:.2f}")

import random
low=1
high=100
options=("rock","paper","scissors")
cards=["2","3","4","5","6","7","8","9","J","K","L"]
# number=random.randint(low,high)
# number=random.random() #floating point return garcha random.random garyo vane
# option=random.choice(options)
random.shuffle(cards) #jun pani print hunu sakxxa random huncha chaye letter huncha ki chaye number
print(cards)
number=random.randint(1,6)  #Jun number pani print garcha 1 dheki 10 samma hai ta
print(number)

print(help(random))


#Python number guessing game

import random

lowest=1
highest=100
answer=random.randint(lowest,highest)
guesses=0
is_running=False
print("Python number Guessing game")
print(f"Select a number between {lowest} and {highest}")


while is_running==True:
    guess=input("Enter your guess:")
    if guess.isdigit():
        guess=int(guess)
        guesses += 1
    else:
        print("Inavalid guess")