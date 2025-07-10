# # indexing= accessing elements of a sequence using[] (indexing operator) [start:end:step] 

# credit_number="1234-5678-9045"
# # credit=credit_number[0:4]
# # credit=credit_number[5:]  # : yesto vyo vane last samma print garcha 
# # credit=credit_number[-2]
# credit=credit_number[::] # yesto halyo vane stsrt to end samma print huncha
# credit=credit_number[::3]
# print(credit)


# credit_number="1234-5678-8976"
# last_digits=credit_number[-4:]
# last_digits=credit_number[::-1]
# print(last_digits)



# #Format specifiers={value:flags} format a value based on what flags are inserted


# # .(number)f=round to that many decimal places(fixed point)
# # .(number)=allocate that many spaces
# # 03.=allocate and zero pad that many spaces
# # :<=left justify
# # :>=right justify
# # :^=center align
# # :+= use a plus sign to indicate postive value
# # :=  =place sign to indicate postive value
# # :=Insert a space before positive numbers
# # :,=comma separator

# price=3.123
# price1=-987.67
# price2=12.34
# price3=12.34
# price4=12.34
# price5=12.345
# price6=345.35345
# price7=500000.678
# print(f"Price is ${price:.2f}")  #:.2f ley point pachi ko number lai 2 ta digit ma banaucha f vaneko floating ho
# print(f"Price1 is ${price1:10}")#10 halim vane 10 ota space craete huncha tehi line maa
# print(f"Price2 is ${price2:010}") #010 halim vane aagdii ko number ma zero create huncha
# print(f"Price2 is ${price2:+}") #agdii posiive sign aaucha
# print(f"Price2 is ${price2:^10}")  #^ yesle bicha ma leucha
# print(f"Price2 is ${price2:>10}")  #> right side ma lancha
# print(f"Price2 is ${price2:<10}") #,Left side ma lagcha 
# print(f"Price7 is ${price7:,}") #Thousand ma comma halcha bicha ma
# print(f"Price7 is ${price7:+,.2f}") #Thousand ma comma halcha bicha ma


# #While loop=execute some code WHILE some condition remains true

# name=input("Enter your name:")
# while name=="":
#  print("You didnt enter your name")
#  name=input("Enter your name:")

# print(f"Hello {name}")

# num=int(input("Enter a # number 1-10:"))

# while num<1 or num>10:
#     print(f"{num}is not valid")
#     num=int((input("Enter a # between 1-10:")))
    
#     print(f"Your number is {num}")

# principle=0
# rate=0
# time=0
# while principle <=0:
#    principle=float(input("Enter the principle amount:"))
#    if principle <=0:
#         print("The principle amount is not entered")
        
# while rate<=0:
#     rate=float(input("Enter the interest rate:"))
#     if rate <=0:
#         print("The rate is not entered")
        
# while time <=0:
#     time=float(input("Enter the time:"))
#     if time <=0:
#         print("The time is not entered")
# total=principle*pow((1+rate/100),time)
# print(total)

# For loops=execute a block a fixed number of times. You can iterate over a range, String, Sequence etc.

# for alphabet in range(1,100):
#     print(alphabet)
# for alphabet in reversed (range(1,100)): #reversed means paxadi dheki print garcha
#     print(alphabet)
# for x in range(1,100,2): # last ma 2 cha ni 1 pachi 3 print garcha euta number chodera print garcha
#     print(x)

# credit_card="1234-567-890-23"
# for i in credit_card:    #credit card ko sabai number print garcha
#     print(i)
    
# for x in range(1,22):
#     if x==13:
#         # break #13 vanda mathy jadaina
#         continue #13 lai hataucha ani aru print garcha   break ani continue euta keywords ho
#     else:
#      print(x)
import time
my_time=int(input("Enter times:"))
for x in range(1,my_time):
    print(x)
    time.sleep(1)  #3 sec pachi excute huncha
print("Times up")

my_time=int(input("Enter times:"))
for x in range(my_time,0,-1):
    print(x)
    time.sleep(1)  #3 sec pachi excute huncha
print("Times up")