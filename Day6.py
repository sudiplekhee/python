#indexing= accessing elements of a sequence using[] (indexing operator) [start:end:step] 

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



##Format specifiers={value:flags} format a value based on what flags are inserted


#.(number)f=round to that many decimal places(fixed point)
#.(number)=allocate that many spaces
#03.=allocate and zero pad that many spaces
# :<=left justify
# :>=right justify
# :^=center align
# :+= use a plus sign to indicate postive value
# :=  =place sign to indicate postive value
# :=Insert a space before positive numbers
# :,=comma separator

price=3.123
price1=-987.67
price2=12.34
price3=12.34
price4=12.34
price5=12.345
price6=345.35345
price7=500000.678
print(f"Price is ${price:.2f}")  #:.2f ley point pachi ko number lai 2 ta digit ma banaucha f vaneko floating ho
print(f"Price1 is ${price1:10}")#10 halim vane 10 ota space craete huncha tehi line maa
print(f"Price2 is ${price2:010}") #010 halim vane aagdii ko number ma zero create huncha
print(f"Price2 is ${price2:+}") #agdii posiive sign aaucha
print(f"Price2 is ${price2:^10}")  #^ yesle bicha ma leucha
print(f"Price2 is ${price2:>10}")  #> right side ma lancha
print(f"Price2 is ${price2:<10}") #,Left side ma lagcha 
print(f"Price7 is ${price7:,}") #Thousand ma comma halcha bicha ma
print(f"Price7 is ${price7:+,.2f}") #Thousand ma comma halcha bicha ma


##While loop=execute some code WHILE some condition remains true

name=input("Enter your name:")
while name=="":
 print("You didnt enter your name")
 name=input("Enter your name:")

print(f"Hello {name}")