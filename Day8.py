import random

# options=("rock","paper","scissors")
# player= None
# computer=random.choice(options)
# player=input("Enter a choice (rock,paper,scissors):")
# print(f"Player:{player}")
# print(f"Computer:{computer}")

options=("rock","paper","knife")
player= None
computer=random.choice(options)
running=True
player=input("Enter a choice(rock,paper,knife):")
print(f"player:{player}")
print(f"computer:{computer}")

if player==computer:
    print("It's a tie!")
elif player=="rock" and computer=="scissors":
    print("You win!")
elif player=="paper" and computer=="rock":
    print("you win!")
elif player== "scissors" and computer=="paper":
    print("You win?!")
else:
    print("You lose!")



