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

for alphabet in range(1,100):
    print(alphabet)
for alphabet in reversed (range(1,100)): #reversed means paxadi dheki print garcha
    print(alphabet)
for x in range(1,100,2): # last ma 2 cha ni 1 pachi 3 print garcha euta number chodera print garcha
    print(x)

credit_card="1234-567-890-23"
for i in credit_card:    #credit card ko sabai number print garcha
    print(i)
    
for x in range(1,22):
    if x==13:
        # break #13 vanda mathy jadaina
        continue #13 lai hataucha ani aru print garcha   break ani continue euta keywords ho
    else:
     print(x)
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

import time

my_time=int(input("Enter the times in second:"))

for x in range(my_time,0,-1):
    seconds=x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Times up!")


#nested loop = A loop within another loop(outer,inner)
#outer loop:
#inner loop:
for x in range(0,10):
    print(x,end="")  #end ko kam k ho vanda kheri straight lines ma print garne 

for x in range(4):
    for y in range(1,10):
        print(y,end="")
        print()  #print() sabai new line ma aaucha
        
rows=int(input("Enter the rows: "))
colums=int(input("Enter the colums: "))
symbol=input("Enter symbol: ")

for x in range(rows):
    for y in range(colums):
        print(symbol, end="")
    print()


#Collection =single "variable" used to store multiple values
# list=[] ordered and changeable .DFuplicates Ok
# Set={} unordered and immutable, But add/remove ok.No Duplicates
# Tuple=() ordered and unchangable Duplicates Ok fASTER


#List
fruits= ["Apple","Ball","cow","hello"]
print(fruits[0:2])
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("Apple" in fruits)  #True or false return garcha []yesko bhitra cha ki chaina ani true and false return garcha
fruits[0]="Okasy" #Apple ko index 0 honita tele apple lai okasy banaucha change garcha
fruits.append("Sudip") #Add garcha
for x in fruits:
fruits.remove("Apple") #sudip string hataucha
fruits.insert(0,"Lekhee") # 0 index pachi insert garcha
fruits.sort()#alphabetically order ma milaucha 
fruits.reverse()#paxadi dheki agdii leucha
fruits.clear() #sabai clear garcha 
print(fruits.index("cow")) #index ley kati number index ma cha vancha
print(fruits.count("cow")) #count ley kati ota cow cha vanera count garcha

#Set
fruits={"apple","banana","buffalo","dog"}    #set ma {} yesto bracket use huncha jati jati code execute garchum teti palta value yeta uta huncha matlan zigzag

print(fruits)