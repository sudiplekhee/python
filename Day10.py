# import random
# import string

# chars=string.punctuation + string.digits + string.ascii_letters  # yo line ley special charcter haru banaucha encrypted form ma banaucha
# chars=list(chars) #single single letter banayera print garcha
# key=chars.copy()
# random.shuffle(key)
# print(chars)  
# print(f"chars:{chars}")
# print(f"keys:{key}")

# #ENCRYPT
# plain_text=input("Enter an message to encrypt:")
# cipher_text=""

# for letter in plain_text:
#     index=chars.index(letter)
#     cipher_text += key[index]
    
# print(f"Original message:{plain_text}")
# print(f"encrypted message:{cipher_text}")

# #Decrypt

# cipher_text=input("Enter a message to encrypt:")
# plain_text=""

# for letter in cipher_text:
#     index=key.index(letter)
#     plain_text +=chars[index]
# print(f"encrypted message:{cipher_text}") 
# print(f"Original message:{plain_text}")

#Hangman in python

import random
words=("mango","apple","banana","graphs","pineapple")


#dictionary of key:()
hagman_art={0: ("  ",
                "  ",
                "  "),
            1: (" o ",
                "  ",
                "  "), 
            2: (" o ",
                " | ",
                "   "), 
            3: (" o ",
                " /| ",
                "   "), 
            4: (" o ",
                " \|/ ",
                "  "), 
            5:(" o ",
                " \|/ ",
                " / "),
            6: (" o ",
                " \|/ ",
                " /\\ ")
}
def display_name(wrong_guesses):
    for line in hagman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    pass
def display_answer(answer):
    pass
def main():
    answer=random.choice(words)
    print(answer)
    hint=["_"] * len(answer)
    print(hint)
    wrong_guesses=0
    guessed_letters=set()
    is_running= True
    
    while is_running:
        display_name(wrong_guesses)
        display_hint(hint)
        guess=input("Enter a letter:").lower()

if __name__ == "__main__":
    main()
                
      
      
      
                   