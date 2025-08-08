# #exception= An event that interrupts the flow of a program (Zero divisionError,TypeError,ValueError)
# #1.try 2.except, 3.finally

try:
    number=int(input("Enter the number:"))
    print(1 / number)
except ZeroDivisionError:
    print("you cant divide by zero")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong!")
finally:
    print("Do something clear here")
    
    
# #Python file detection

#os means operating system
import os

file_path="C:\\Users\\SUDIP\\Desktop\\test.txt"
if os.path.exists(file_path):  #exists means builtin function
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exists")
    
#python writting files (.txt,.json,.csv)

# txt_data="I like apple banana"
employee=["sudip","nikhil","sumit","nishanta"]
file_path="C:\\Users\\SUDIP\\Desktop\\output.txt"  #path diye pachi tyo ma gayera bancha
try:
 with open (file=file_path,mode="a")as file:  #w means write x means file exitserror  and a means append the data
    # file.write(employee)
    for employees in employee:
        file.write(employees+"\n")
    print(f"txt file '{file_path}' is created")
except FileExistsError:
    print("That file already exists")

Now json is started
import json
employee={
    "name":"sudip",
    "age":"21",
    "comapny":"Digital pathsala"
}
file_path="C:\\Users\\SUDIP\\Desktop\\output.txt" 
try:
 with open (file=file_path,mode="a")as file:  #w means write x means file exitserror  and a means append the data
    json.dump(employee, file,indent=4)
   
    print(f"json file '{file_path}' is created")
except FileExistsError:
    print("That file already exists")

import json
import csv
employees=[["Name","age","Job"],
           ["Sudip",21,"Manager"],
           ["Nikhil",20,"Cyber"],
           ["Sumit",22,"ml"]]
file_path="C:\\Users\\SUDIP\\Desktop\\output.csv" 
try:
 with open (file=file_path,mode="a",newline="")as file:  #w means write x means file exitserror  and a means append the data
    writer=csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"csv file '{file_path}' is created")
except FileExistsError:
    print("That file already exists")