# countdown timer with ascii art project!
import time
import os
from colorama import Fore, init

init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# dictionary mapping numbers to their ascii art version
numbers = {
    0: r"""   
   ___  
  / _ \ 
 | | | |
 | |_| |
  \___/ 
        """,
    1: r"""   
  _ 
 / |
 | |
 | |
 |_|
       """,
    2: r"""   
  ____   
 |___ \  
   __) | 
  / __/  
 |_____| 

       """,

    3: r"""   
  _____ 
 |___ / 
   |_ \ 
  ___) |
 |____/ 
       """,

    4: r"""   
  _  _   
 | || |  
 | || |_ 
 |__   _|
    |_|  
       """,

    5: r"""   
  ____  
 | ___| 
 |___ \ 
  ___) |
 |____/ 
       """,

    6: r"""   
   __   
  / /_  
 | '_ \ 
 | (_) |
  \___/ 

       """,

    7: r"""   
  _____ 
 |___  |
    / / 
   / /  
  /_/   
       """,

    8: r"""   
   ___  
  ( _ ) 
  / _ \ 
 | (_) |
  \___/ 

       """,

    9: r"""   
   ___  
  / _ \ 
 | (_) |
  \__, |
    /_/  
       """}

# alright so i got all the numbers, now i have got to find out how to print them next to each other

###prints 9 to 0!
# for i in range(9, -1, -1):
#     print(numbers[i])
#     time.sleep(1)
#     clear_screen()


# hold_for_me = ""
# for character in numbers[0]:
#
#     if not character in "\n":
#         hold_for_me += character
#     else:
#         for character2 in numbers[1]:
#
#             if not character2 in "\n":
#                 hold_for_me += character2
#             else:
#                 break
#
#         hold_for_me += "\n"
#

# print(hold_for_me)
#
#
# print(numbers[0][50])

# print(numbers[0].split("\n"))
# print(numbers[1].split("\n"))
#
# zipped = zip(numbers[0].split("\n"), numbers[1].split("\n"))
#
# print(list(zipped))

#
# for a, b in zip(numbers[0].split("\n"), numbers[1].split("\n")):
#     print(f"{a}{b}")

# length = input("How many seconds?")
#
#
# first_number = int(length[0])
# second_number = int(length[1])
# count = int(length)
#
# while count >= 0:
#     for a, b in zip(numbers[first_number].split("\n"), numbers[second_number].split("\n")):
#         print(f"{Fore.RED + a}{Fore.LIGHTRED_EX + b}")
#         if second_number == 0:
#             first_number -= 1
#             second_number += 10
#
#     second_number -= 1
#     count -= 1
#     time.sleep(1)
#     clear_screen()
#


# i had to look up how to add triple quotes (the ascii art) next to eachother
#     for a, b in zip(numbers[0].splitlines(), numbers[1].splitlines()):
#         print(f"{a}{b}")
# after a couple of minutes, i know completely understand how it works.

# import math
#
# totals = 5.5 #5 minutes and 30 seconds
# minutes = math.floor(totals)
# seconds = round((totals - minutes) * 60)
#
# print(minutes)
# print(seconds)
#
# total_seconds = minutes * 60 + seconds
#
# print(total_seconds)

# success

# for i in range(0, total_seconds):
#     if seconds == -1:
#         seconds += 60
#         minutes -= 1
#
#     if seconds < 10:
#         print(f"{minutes}:0{seconds}")
#     else:
#         print(f"{minutes}:{seconds}")
#     seconds -= 1
#     time.sleep(0.3)


# assigning the digits for the seconds display
# if seconds != 0:
#     first_number = int(seconds[0]) # 3
#     second_number = int(seconds[1]) # 0
# else:
#     first_number = 0
#     second_number = 0


# def display_seconds():
#
#     global first_number, second_number
#     while not first_number == -1 and not second_number == -1:
#         for a, b in zip(numbers[first_number].split("\n"), numbers[second_number].split("\n")):
#             print(f"{Fore.RED + a}{Fore.LIGHTRED_EX + b}")
#             if second_number == 0:
#                 first_number -= 1
#                 second_number += 10
#
#         second_number -= 1
#         time.sleep(1)
#
#
#
#
# def display_all():
#     global first_number, second_number, minutes
#
#     for a, b in zip(numbers[minutes].split("\n"), display_seconds()):
#         if first_number == -1 and second_number == -1:
#             first_number += 6
#             minutes -= 1
#         else:
#             print(f"{a}{b}")

# display_all()
# we are going to put this together with the minutes
# the parameter will be the result of splitting the user input (5.5 minutes example)

# def display_minutes()


spacing = r"""
  _ 
 (_)

  _ 
 (_)

"""
# import math
#
# #asks user for the time
# how_long = input("Set a time (5.5 for example)\n>") # if 5.5
#
# #converts it into a float
# minutes_and_seconds = float(how_long) # 5.5
#
# #removes the decimals for minutes
# minutes = math.floor(minutes_and_seconds) # 5
#
# #removes the integer and converts it to seconds (* 60)
# seconds = str(round((minutes_and_seconds - minutes) * 60)) # 30
# print(seconds)
#
#
# first_number = int(seconds[0]) # 3
#
# print(seconds)


# user_input_minutes = int(input("how many minutes?\n>"))
# minutes = user_input_minutes
# user_input_seconds = input("how many seconds?\n>")
#
# first_number = 0
#
# try:
#     first_number = int(user_input_seconds[0])
#     second_number = int(user_input_seconds[1]) # 0
# except IndexError:
#     second_number = first_number
#     first_number = 0
#
# total_ticks = minutes * 60 + int(user_input_seconds)

# display prints the numbers of input we gotta lower the amount number
# display = numbers[minutes], spacing, numbers[first_number], numbers[second_number] #5, 3, 0
# for number in zip(*(number.splitlines() for number in display)):
#     print("".join(number))


# for i in range(0, total_ticks):
#     if seconds == -1:
#         seconds += 60
#         minutes -= 1
#
#     if seconds < 10:
#         print(f"{minutes} {seconds}")
#     else:
#         print(f"{minutes} {seconds}")
#     seconds -= 1
#     time.sleep(0.3)


user_input_minutes = int(input("how many minutes?\n>"))
minutes = user_input_minutes
user_input_seconds = input("how many seconds?\n>")

first_number = 0

try:
    first_number = int(user_input_seconds[0])
    second_number = int(user_input_seconds[1])  # 0
except IndexError:
    second_number = first_number
    first_number = 0

total_ticks = minutes * 60 + int(user_input_seconds)

for i in range(0, total_ticks):

    if second_number == -1:
        first_number -= 1
        second_number += 10

    if first_number == -1:
        minutes -= 1
        first_number += 6

    display = numbers[minutes], spacing, numbers[first_number], numbers[second_number]
    print("_________________________________")
    for number in zip(*(number.splitlines() for number in display)):
        print("".join(number))
    print("_________________________________")
    second_number -= 1
    time.sleep(0.5)
    clear_screen()

# succes


