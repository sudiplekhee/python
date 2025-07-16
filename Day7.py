#Shopping card program

foods=[]
prices=[]
total=0
while True:
    food=input("Enter a food to buy(q to quit):")
    if food.lower()=="q":  # lower halim nita capital Q pani support garcha
        break
    else:
        price=float(input(f"Enter the price of a {food}:$"))
        foods.append(food)
        prices.append(price)
for food in foods:
    print(food,end=" ")
    
for price in prices:
    total += price
    print()
    print(f"Yout Total is :${total}")


# Toady we will describe about 2D list
fruits=    ["apple","banana","orange","mango"]
vegetables=["ce4lery","carrots","potatoes"]
meats=     ["chicken","fish","turkey"]

groceries=[fruits,vegetables,meats]

# print(groceries[0])

print(groceries[0][1]) #row zero column one

groceries=[  ["apple","banana","orange","mango"],["celery","carrots","potatoes"],["chicken","fish","turkey"]]

for collection in groceries:
    for food in collection:  #we use nested loop 
     print(food,end=" ")
    print()     #We use print() for arrangi8ng in proper in way 

num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#"))
for row in num_pad:
    for everyrow in row:
     print(everyrow,end=" ")
    print()


#Python Quiz game


question=()
options=((),(),(),())

answers=()
guesses=[]
score=0
question_num=0