#Madlibs game
#word game where you create a story
#by filling in blanks with random words
adjective=input("Enter an adjective (descrition):")
noun1=input("Enter a noun (person,place,thing):")
adjective2=input("Enter an adjective (descrition):")
verb1=input("Enter a verb ending with ''ing:")
adjective3=input("Enter an adjective (descrition):")


print(f"Today I went to a {adjective} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")


friends=10
friends=friends+1
friends += 1
friends=friends-1
friends=friends+1
friends -= 1
friends= friends * 2
friends *= 3
friends= friends /2
friends /= 2
friends=friends**2
friends **= 2
remainder=friends % 3
print(remainder)

x=3.14
y=4
z=5

result=round(x) #round function means to find the nearest number
result=abs(y) #abs means absolute value
result=pow(4,3)
result=max(x,y,z)
result=min(x,y,z)
print(result)