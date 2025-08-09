# # #exception= An event that interrupts the flow of a program (Zero divisionError,TypeError,ValueError)
# # #1.try 2.except, 3.finally

# try:
#     number=int(input("Enter the number:"))
#     print(1 / number)
# except ZeroDivisionError:
#     print("you cant divide by zero")
# except ValueError:
#     print("Enter only numbers please")
# except Exception:
#     print("Something went wrong!")
# finally:
#     print("Do something clear here")
    
    
# # #Python file detection

# #os means operating system
# import os

# file_path="C:\\Users\\SUDIP\\Desktop\\test.txt"
# if os.path.exists(file_path):  #exists means builtin function
#     print(f"The location '{file_path}' exists")
#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("That location doesn't exists")
    
# #python writting files (.txt,.json,.csv)

# # txt_data="I like apple banana"
# employee=["sudip","nikhil","sumit","nishanta"]
# file_path="C:\\Users\\SUDIP\\Desktop\\output.txt"  #path diye pachi tyo ma gayera bancha
# try:
#  with open (file=file_path,mode="a")as file:  #w means write x means file exitserror  and a means append the data
#     # file.write(employee)
#     for employees in employee:
#         file.write(employees+"\n")
#     print(f"txt file '{file_path}' is created")
# except FileExistsError:
#     print("That file already exists")

# Now json is started
# import json
# employee={
#     "name":"sudip",
#     "age":"21",
#     "comapny":"Digital pathsala"
# }
# file_path="C:\\Users\\SUDIP\\Desktop\\output.txt" 
# try:
#  with open (file=file_path,mode="a")as file:  #w means write x means file exitserror  and a means append the data
#     json.dump(employee, file,indent=4)
   
#     print(f"json file '{file_path}' is created")
# except FileExistsError:
#     print("That file already exists")

# import json
# import csv
# employees=[["Name","age","Job"],
#            ["Sudip",21,"Manager"],
#            ["Nikhil",20,"Cyber"],
#            ["Sumit",22,"ml"]]
# file_path="C:\\Users\\SUDIP\\Desktop\\output.csv" 
# try:
#  with open (file=file_path,mode="a",newline="")as file:  #w means write x means file exitserror  and a means append the data
#     writer=csv.writer(file)
#     for row in employees:
#         writer.writerow(row)
#     print(f"csv file '{file_path}' is created")
# except FileExistsError:
#     print("That file already exists")


#python reading files(.txt,.json,.csv)

# file_path="C:\\Users\\SUDIP\\Desktop\\output"
# try:
#  with open(file_path, "r") as file:
#     content=file.read()
#     print(content)
# except FileNotFoundError:
#     print("File was not found")
# except PermissionError:
#     print("You do not have  permission to read this file")

# import json

# file_path="C:\\Users\\SUDIP\\Desktop\\output.json"
# try:
#  with open(file_path, "r") as file:
#     content=json.load(file)
#     print(content["name"])
# except FileNotFoundError:
#     print("File was not found")
# except PermissionError:
#     print("You do not have  permission to read this file")

# import csv
# file_path="C:\\Users\\SUDIP\\Desktop\\output.csv"
# try:
#  with open(file_path, "r") as file:
#     content=csv.reader(file)
#     for line in content:
#      print(line[1])
# except FileNotFoundError:
#     print("File was not found")
# except PermissionError:
#     print("You do not have  permission to read this file")

# import datetime

# date=datetime.date(2025,6,8)
# today=datetime.date.today()

# time=datetime.time(12,23,0)
# now=datetime.datetime.now()

# now=now.strftime("%H:%M:%S %d-%m-%Y")
# print(now)

# target_datetime=datetime.datetime(2020,1,2,12,30,1)
# current_datetime=datetime.datetime.now()

# if target_datetime < current_datetime:
#     print("Target date passed")
# else:
#     print("Target date has not passed")


#Python alarm clock

import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file="Alarm.mp3"
    is_running=True
    
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time==alarm_time:
            print("Wake up")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running=False
        time.sleep(1)
       
if __name__ =="__main__":
    alarm_time=input("Enter the alarm time (HH:MM:SS):")
    set_alarm(alarm_time)