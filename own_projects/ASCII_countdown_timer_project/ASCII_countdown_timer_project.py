# countdown timer with ascii art project!
import time
import os
from array import ArrayType


# from colorama import Fore, init
# init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ascii_art converter
def ascii_art(character):  # , font type

    numbers = {
        "0":
            r"""   
               ___  
              / _ \ 
             | | | |
             | |_| |
              \___/ 
            """,
        "1": r"""   
  _ 
 / |
 | |
 | |
 |_|
       """,
        "2": r"""   
  ____   
 |___ \  
   __) | 
  / __/  
 |_____| 

       """,

        "3": r"""   
  _____ 
 |___ / 
   |_ \ 
  ___) |
 |____/ 
       """,

        "4": r"""   
  _  _   
 | || |  
 | || |_ 
 |__   _|
    |_|  
       """,

        "5": r"""   
  ____  
 | ___| 
 |___ \ 
  ___) |
 |____/ 
       """,

        "6": r"""   
   __   
  / /_  
 | '_ \ 
 | (_) |
  \___/ 
       """,

        "7": r"""   
  _____ 
 |___  |
    / / 
   / /  
  /_/   
       """,

        "8": r"""   
   ___  
  ( _ ) 
  /|_|\ 
 | (_) |
  \___/ 
       """,

        "9": r"""   
   ___  
  / _ \ 
 | (_) |
  \__, |
    /_/  
       """,
        "spacing":
            r"""
              _ 
             (_)
            
              _ 
             (_)
            
            """}

    return numbers[character]  # [fonttypeindex]


# asks for and returns the user inputted minutes
def get_minutes():
    while True:
        user_input = input("How many minutes?\n> ")
        try:
            user_input = int(user_input)
            if user_input < 59:
                return user_input
            else:
                print("Invalid input (Enter a number between 0 - 59)\nPress \"Enter\" to continue.")

        except ValueError:
            input("Invalid input (Enter a number)\nPress \"Enter\" to continue.")


# asks for and returns the user inputted seconds
def get_seconds():
    while True:
        user_input = input("How many seconds?\n> ")

        try:
            user_input = int(user_input)
            if user_input < 3600:
                return user_input
            else:
                print("Invalid input (Enter a number between 0 - 3600)\nPress \"Enter\" to continue.")

        except ValueError:
            input("Invalid input (Enter a number)\nPress \"Enter\" to continue.")


# countdown using all the previous functions
def countdown_timer():
    # calculates total time and converts
    time_in_seconds = get_minutes() * 60 + get_seconds()
    minutes = time_in_seconds // 60
    seconds = time_in_seconds % 60

    # the timer itself
    for i in range(time_in_seconds, -1, -1):

        # countdown logic
        if seconds == -1:
            minutes -= 1
            seconds += 60

        # what the user sees
        display = ascii_art(str(minutes).zfill(2)[0]), ascii_art(str(minutes).zfill(2)[1]), ascii_art(
            "spacing"), ascii_art(str(seconds).zfill(2)[0]), ascii_art(str(seconds).zfill(2)[1])

        # prints the ascii art next to each other
        for number in zip(*(number.splitlines() for number in display)):
            print("".join(number))

        # if both are 0 print message, could add sound in the future
        if 0 == minutes == seconds:
            input("time's up!")  # possible alarm

        # countdown logic and clear screen
        seconds -= 1
        time.sleep(1)
        clear_screen()

    input("time's up!")  # possible alarm


countdown_timer()


















