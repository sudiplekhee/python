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


questions = (
    "How many elements in periodic table?:",
    "Which animal lays the largest eggs?:",
    "What is the most abundant gas in Earth's atmosphere?:",
    "How many bones are in the human body?:",
    "Which planet in the solar system is the hottest?:"
)

options = (
    ("A.116", "B.117", "C.118", "D.119"),
    ("A.Whale", "B.Crocodile", "C.Elephant", "D.Ostrich"),
    ("A.Nitrogen", "B.Oxygen", "C.Carbon-dioxide", "D.Hydrogen"),
    ("A.206", "B.207", "C.208", "D.209"),
    ("A.Mercury", "B.Venus", "C.Earth", "D.Jupiter")
)

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("\n------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")
    
    question_num += 1

# Final Score
print("\n==================")
print("      RESULT      ")
print("==================")
print("Correct Answers:", answers)
print("Your Guesses:   ", guesses)
print(f"Your Score: {score}/{len(questions)}")
