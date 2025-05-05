# countdown timer with ascii art project!
import time
import os


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
        ":":
r"""
  _ 
 (_)
    
  _ 
 (_)
"""}

    return numbers[character]  # [fonttypeindex]



def get_hours():
    while True:
        user_input = input("How many hours?\n> ")
        try:
            user_input = int(user_input)
            if 59 >= user_input >= 0:
                return user_input
            else:
                print("Invalid input (Enter a number between 0 - 59)\nPress \"Enter\" to continue.")

        except ValueError:
            input("Invalid input (Enter a number)\nPress \"Enter\" to continue.")



# asks for and returns the user inputted minutes
def get_minutes():
    while True:
        user_input = input("How many minutes?\n> ")
        try:
            user_input = int(user_input)
            if 59 >= user_input >= 0:
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
            if 59 >= user_input >= 0:
                return user_input
            else:
                print("Invalid input (Enter a number between 0 - 59)\nPress \"Enter\" to continue.")

        except ValueError:
            input("Invalid input (Enter a number)\nPress \"Enter\" to continue.")


# countdown using all the previous functions
def countdown_timer():
    # calculates total time and converts
    time_in_seconds = get_hours() * 3600 + get_minutes() * 60 + get_seconds()
    hours = time_in_seconds // 3600
    minutes = time_in_seconds // 60
    seconds = time_in_seconds % 60

    # the timer itself
    for i in range(time_in_seconds, -1, -1):

        # countdown logic
        if seconds == -1:
            minutes, seconds = divmod(i, 60)
            hours, minutes = divmod(minutes, 60)

        colon = ascii_art(":")
        # assigning hour digits
        hour_tens = ascii_art(str(hours).zfill(2)[0])
        hour_units = ascii_art(str(hours).zfill(2)[1])
        # assigning minute digits
        minute_tens = ascii_art(str(minutes).zfill(2)[0])
        minute_units = ascii_art(str(minutes).zfill(2)[1])
        # assigning digits
        second_tens = ascii_art(str(seconds).zfill(2)[0])
        second_units = ascii_art(str(seconds).zfill(2)[1])

        # what the user sees
        display = hour_tens, hour_units, colon, minute_tens, minute_units, colon, second_tens, second_units

        # prints the ascii art next to each other
        for number in zip(*(number.splitlines() for number in display)):
            print("".join(number))

        # countdown logic and clear screen
        seconds -= 1
        time.sleep(1)
        clear_screen()

    input("time's up!")  # possible alarm





def logo():
    print(r"""
     _    ____   ____ ___ ___      _    ____ _____   _____ ___ __  __ _____ ____  
    / \  / ___| / ___|_ _|_ _|    / \  |  _ \_   _| |_   _|_ _|  \/  | ____|  _ \ 
   / _ \ \___ \| |    | | | |    / _ \ | |_) || |     | |  | || |\/| |  _| | |_) |
  / ___ \ ___) | |___ | | | |   / ___ \|  _ < | |     | |  | || |  | | |___|  _ < 
 /_/   \_\____/ \____|___|___| /_/   \_\_| \_\|_|     |_| |___|_|  |_|_____|_| \_\                          
    """)


def menu_options():
    print(85 * "─")
    print("1. Countdown")
    print("2. Settings (COMING SOON)")
    print(25 * "─")


def application():

    while True:
        logo()
        menu_options()
        user_input = input("> ").strip().lower()
        clear_screen()

        if user_input in ["1", "countdown"]:
            countdown_timer()
        else:
            input("Invalid input.")
            clear_screen()



application()













