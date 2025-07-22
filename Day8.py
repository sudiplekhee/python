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


import random
# ● ┌ ┐ │ └ ┘
"┌---------┐ "
"│         │"
"│         │"
"│         │"
"└---------┘"

dice_art={
    1:("┌---------┐",  #These all are key values pair
       "│         │",
       "│    #    │",
       "│         │",
       "└---------┘"),
    2:("┌---------┐",  #These all are key values pair
       "│   #     │",
       "│         │",
       "│        ●│",
       "└---------┘"),
    3:("┌---------┐",  #These all are key values pair
       "│  ●      │",
       "│    ●    │",
       "│       ● │",
       "└---------┘"),
    4:("┌---------┐",  #These all are key values pair
       "│  ●    ● │",
       "│         │",
       "│  ●    ● │",
       "└---------┘"),
    5:("┌---------┐",  #These all are key values pair
       "│  ●    ● │",
       "│     ●   │",
       "│  ●    ● │",
       "└---------┘"),
 6:   ("┌---------┐",  #These all are key values pair
       "│ ●  ●  ● │",
       "│         │",
       "│ ●  ●  ● │",
       "└---------┘")
}
dice=[]
total=0
num_of_dice=int(input("How many dice?:"))
for die in range(num_of_dice):
 dice.append(random.randint(1, 6))
print(dice)

for die in range(num_of_dice):
   for line in dice_art.get(dice[die]):
      print(line)
for line in range(5):
   for die in dice:
      print(dice_art.get(die)[line], end="")
   print()

for die in dice:
   total += die
print(f"Total:{total}")


# #function =A block of reusable code
# place()after the function name to invoke it

def happy_birthday(name,age):
   print(f"Happy Bithday {name}")
   print(f"You are {age} years old")
   print("Thank you so much")
   
happy_birthday("sudip","21")
happy_birthday("nikhil","20")
happy_birthday("Nishant","22")
    
    
    
    




