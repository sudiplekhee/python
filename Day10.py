import random
import string

chars=string.punctuation + string.digits + string.ascii_letters  # yo line ley special charcter haru banaucha encrypted form ma banaucha
chars=list(chars) #single single letter banayera print garcha
key=chars.copy()
random.shuffle(key)
print(chars)  
print(f"chars:{chars}")
print(f"keys:{key}")

#ENCRYPT
plain_text=input("Enter an message to encrypt:")
cipher_text=""

for letter in plain_text:
    index=chars.index(letter)
    cipher_text += key[index]
    
print(f"Original message:{plain_text}")
print(f"encrypted message:{cipher_text}")

#Decrypt

cipher_text=input("Enter a message to encrypt:")
plain_text=""

for letter in cipher_text:
    index=key.index(letter)
    plain_text +=chars[index]
print(f"encrypted message:{cipher_text}") 
print(f"Original message:{plain_text}")

