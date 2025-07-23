#matchcase statement (switch):An alternative to using 'elif' statements
#Execute some code if a value matches a 'case'
#benefits: cleaner and syntax is more readable

def day_of_week(day):
    if day==1:
        return "It is sunday"
    elif day==2:
        return "It is monday"
    elif day==3:
        return "It is tuesday"
    elif day==4:
        return "It is wednesday"
    elif day==5:
        return "It is thursday"
    elif day==6:
        return "It is friday"
    elif day==7:
        return "It is saturday"
    else:
        return "Not valiodate"
total =day_of_week(2)
print(total)

def day_of_week(day):
 match day:
    case 1:
        return "It is sunday"
    case 2:
        return "It is monday"
    case 3:
        return "It is tuesday"
    case 4:
        return "It is wednesday"
    case 5:
        return "It is thursday"
    case 6:
        return "It is friday"
    case 7:
        return "It is saturday"
    case _:
        return "Not valiodate"
total =day_of_week(9)
print(total)

def isweekend(Day):
    match Day:
        case "Monday":
            return True
        case "sunday":
            return False
        case "Monday":
            return False
        
print(isweekend("Monday"))

def isweekend(Day):
    match Day:
        case "Monday" | "saturday" | "friday":    # | this symbol is known as or operator
            return True
        case "sunday":
            return False
        case "Monday":
            return False
        
print(isweekend("friday"))


#Module= a file containing code you want to include in your program
#use 'import' to include (built-in or your own)
#useful to break up a large program reuable separate files

print(help("modules"))