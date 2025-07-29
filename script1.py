# # def favorite_food(food):
# #     print(f"Your favorite food is {food}")
# # def main():
# #  print("This is script1")
# #  favorite_food("pizza")
# # print("Goodbye")
# # if __name__ == '__main__':
# #     main()
    
    
# #python banking program

# def showbalance():
#     print(f"Your balance is ${balance:.2f}")

# def deposit():
#     amount=input("Enter an amount to be deposited:")
    
#     if amount < 0:
#         print("That's not a valid email")
#         return 0
#     else:
#         return amount

# def withdraw():
#     amount=input("Enter amount to be withdrawn:")
    
#     if amount > balance:
#         print("Insufficient funds")
#         return 0
#     elif amount < 0:
#         print("Amount must be greater than 0")
#         return 0
#     else:
#         return amount
# def main():
#    balance=0
#    is_running=True

# while is_running:
#     print("Banking program")
#     print("1.Show Balance")
#     print("2.Deposit")
#     print("3.withdraw")
#     print("4.Exit")
    
#     choice=int(input("Enter your choice (1-4):"))
    
#     if choice == '1':
#         showbalance(balance)
        
#     elif choice == '2':
#        balance += deposit()
       
#     elif choice == '3':
#        balance -= withdraw(balance)
     
#     elif choice == '4':
#         is_running = False
        
#     else:
#         print("That is not valid choice")
#         print("Thank you ! Have a good Day")
# if __name__ =='__main__':
#     main()


# python slot manchine 
import random
def spin_row():
    symbol=["🍒","🍉","🍋","🔔","✨"]
    return[random.choice(symbol) for _ in range(3)]
    # for symbol in range(3):
    #     results.append(random.choice(symbol))
    # return results
def print_row(row):
    print(" ".join(row)) #by using join method join each element by a space
def get_payout():
    pass
def get_payout(row, bet):
    if row[0] == row[1]==row[2]:
        if row[0] == '🍒':
            return bet *3
        elif row[0] =='🍉':
            return bet *4
        elif row[0]=='🍋':
            return bet *5
        elif row[0] =='🔔':
            return bet *10
        elif row[0] ==' ✨':
            return bet *20
        return 0
def main():
    balance=100
    
    print("************************")
    print("Welcome to python slots")
    print("Symbol:🍒 🍉 🍋 🔔 ✨")
    print("************************")
    
    while balance > 0:
        print(f"Current balance : ${balance}")
        bet=input("Place your bet amount:")
    
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        bet=int(bet)
    
        if bet>balance:
            print("Insufficient funds")
            continue
        if bet<=0:
             print("Bet must be greater than 0")
        balance-=bet
        row=spin_row()
        print("spinning../n")
        print_row(row)
        payout=get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("sorry you lose this round")
        balance+=payout
if __name__=='__main__':
    main()