# def favorite_food(food):
#     print(f"Your favorite food is {food}")
# def main():
#  print("This is script1")
#  favorite_food("pizza")
# print("Goodbye")
# if __name__ == '__main__':
#     main()
    
    
#python banking program

def showbalance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount=input("Enter an amount to be deposited:")
    
    if amount < 0:
        print("That's not a valid email")
        return 0
    else:
        return amount

def withdraw():
    amount=input("Enter amount to be withdrawn:")
    
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
def main():
   balance=0
   is_running=True

while is_running:
    print("Banking program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.withdraw")
    print("4.Exit")
    
    choice=int(input("Enter your choice (1-4):"))
    
    if choice == '1':
        showbalance(balance)
        
    elif choice == '2':
       balance += deposit()
       
    elif choice == '3':
       balance -= withdraw(balance)
     
    elif choice == '4':
        is_running = False
        
    else:
        print("That is not valid choice")
        print("Thank you ! Have a good Day")
if __name__ =='__main__':
    main()


python slot manchine 
