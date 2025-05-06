# countdown timer with ascii art project!
import os
import time
import sys
sys.stdout.reconfigure(encoding="utf-8")

from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ascii_art converter
def ascii_art(character):  # , font type

    numbers = {
"0":r"""   ___   
  / _ \  
 | | | | 
 | |_| | 
  \___/  """,
"1": r"""    _    
   / |   
   | |   
   | |   
   |_|   """,
"2": r"""  ____   
 |___ \  
   __) | 
  / __/  
 |_____| """,
"3": r"""  _____  
 |___ /  
   |_ \  
  ___) | 
 |____/  """,

"4": r"""  _  _   
 | || |  
 | || |_ 
 |__   _|
    |_|  """,

"5": r"""  ____   
 | ___|  
 |___ \  
  ___) | 
 |____/  """,

"6": r"""   __    
  / /_   
 | '_ \  
 | (_) | 
  \___/  """,

"7": r"""  _____  
 |___  | 
    / /  
   / /   
  /_/    """,

"8": r"""   ___   
  ( _ )  
  / _ \  
 | (_) | 
  \___/  """,

"9": r"""   ___   
  / _ \  
 | (_) | 
  \__, | 
    /_/  """,
":": r"""  _ 
 (_)
    
  _ 
 (_)""",
"│": r"""│
│
│
│
│
│"""}

    return numbers[character]  # [fonttypeindex]




def get_hours():

    while True:
        print(logo())
        print(color + "│ How many hours? (Press \"Enter\" to go back)      │")
        user_input = input(color + "└" + 49 * "─" + "┘\n")
        clear_screen()


        if user_input == "":
            break

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
        print(logo())
        print(color + "│ How many minutes? (Press \"Enter\" to go back)    │")
        user_input = input(color + "└" + 49 * "─" + "┘\n")
        clear_screen()

        if user_input == "":
            break
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
        print(logo())
        print(color + "│ How many seconds? (Press \"Enter\" to go back)    │")
        user_input = input(color + "└" + 49 * "─" + "┘\n")
        clear_screen()

        if user_input == "":
            break
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
    try:
        time_in_seconds = get_hours() * 3600 + get_minutes() * 60 + get_seconds()
    except TypeError:
        clear_screen()
        return

    hours = time_in_seconds // 3600
    minutes = hours // 60
    seconds = minutes // 60
    clear_screen()

    # the timer itself
    for i in range(time_in_seconds, -1, -1):

        # countdown logic
        if seconds >= -1:
            minutes, seconds = divmod(i, 60)
            hours, minutes = divmod(minutes, 60)



        colon = ascii_art(":")
        line = ascii_art("│")
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
        display =  line, hour_tens, hour_units, colon, minute_tens, minute_units, colon, second_tens, second_units, line



        # prints the ascii art next to each other

        print("\033[H", end="")
        print(color + "┌" + 62 * "─" + "┐")
        output = ""
        for number in zip(*(number.splitlines() for number in display)):
            output += (color + "".join(number) + "\n")

        output = output.rstrip("\n")
        print(output)
        print(color + "└" + 62 * "─" + "┘")
        # countdown logic and clear screen
        seconds -= 1
        time.sleep(1)


    input("time's up!")  # possible alarm
    clear_screen()




def logo():
    return(
        r"""┌─────────────────────────────────────────────────┐
│     __  __      _____ _                         │
│    |  \/  |_   |_   _(_)_ __ ___   ___ _ __     │
│    | |\/| | | | || | | | '_ ` _ \ / _ \ '__|    │
│    | |  | | |_| || | | | | | | | |  __/ |       │
│    |_|  |_|\__, ||_| |_|_| |_| |_|\___|_|       │
│            |___/                                │
├─────────────────────────────────────────────────┤""")

def scrolling_text(sentence):
    for character in sentence:
        sys.stdout.write(color + character)
        sys.stdout.flush()
        time.sleep(0.01)
    # print(color + "\n│ Press \"Enter\" to start.                         │")
    # input(color + "└" + 49 * "─" + "┘")
    clear_screen()



def menu_options(menu_type):
    global menu_display




    if menu_type =="main_menu":
        menu_display = "Main Menu"
        print(color + f"│{menu_display} {" " * (48 - len(menu_display))}│")
        print(color + "│ [1] Start                                       │")
        print(color + "│ [2] Settings                                    │")
        print(color + "│ [3] Exit                                        │")
        print(color + "└" + 49 * "─" + "┘")
    elif menu_type =="settings_menu":
        menu_display = "< Main Menu"
        print(color + f"│{menu_display} {" " * (48 - len(menu_display))}│")
        print(color + "│ [1] Change Font                                 │")
        print(color + "│ [2] Change Color                                │")
        print(color + "│ [3] Back                                        │")
        print(color + "└" + 49 * "─" + "┘")
    elif menu_type == "color_menu":
        menu_display = "< Settings Menu"
        print(color + f"│{menu_display} {" " * (48 - len(menu_display))}│")
        print(color + f"│ {(Fore.RED + "[1] Red")}                                         {color + "│"}")
        print(color + f"│ {Fore.GREEN + "[2] Green"}                                       {color + "│"}")
        print(color + f"│ {Fore.YELLOW + "[3] Yellow"}                                      {color + "│"}")
        print(color + f"│ {Fore.BLUE + "[4] Blue"}                                        {color + "│"}")
        print(color + f"│ {Fore.MAGENTA + "[5] Magenta"}                                     {color + "│"}")
        print(color + f"│ {Fore.CYAN + "[6] Cyan"}                                        {color + "│"}")
        print(color + f"│ {Fore.WHITE + "[7] Exit"}                                        {color + "│"}")
        print(color + "└" + 49 * "─" + "┘")
    elif menu_type == "clock_menu":
        menu_display = "< Main Menu"
        print(color + f"│{menu_display} {" " * (48 - len(menu_display))}│")
        print(color + "│ [1] Count Up                                    │")
        print(color + "│ [2] Count Down                                  │")
        print(color + "│ [3] Back                                        │")
        print(color + "└" + 49 * "─" + "┘")

def choice_handling():
    global current_menu, color
    while True:
        user_input = input(color + "> ").strip().lower()
        clear_screen()

        if current_menu == "main_menu":
            if user_input == "1":
                current_menu = "clock_menu"
            elif user_input == "2":
                current_menu = "settings_menu"
            elif user_input == "3":
                exit() # gotta make a function for this still

        elif current_menu == "settings_menu":
            if user_input == "1":
                ...
            elif user_input == "2":
                current_menu = "color_menu"
            elif user_input == "3":
                current_menu = "main_menu"
        elif current_menu == "color_menu":
            if user_input in ["1"]:
                color = Fore.RED
            elif user_input in ["2"]:
                color = Fore.GREEN
            elif user_input in ["3"]:
                color = Fore.YELLOW
            elif user_input in ["4"]:
                color = Fore.BLUE
            elif user_input in ["5"]:
                color = Fore.MAGENTA
            elif user_input in ["6"]:
                color = Fore.CYAN
            elif user_input == "7":
                current_menu = "settings_menu"
        elif current_menu == "clock_menu":
            if user_input == "1":
                countup_timer()
            elif user_input == "2":
                countdown_timer()
            elif user_input == "3":
                current_menu = "main_menu"
        else:
            input("Invalid input.")
        clear_screen()
        break



def application():
    global color, current_menu, menu_display
    color = Fore.WHITE

    current_menu = "main_menu"
    menu_display = "Main Menu"
    # scrolling_text(logo())

    while True:
        print(color + logo())
        menu_options(current_menu)
        choice_handling()

def countup_timer():
    # calculates total time and converts

    hours = 0
    minutes = 0
    seconds = 0


    # the timer itself
    while True:

        # countdown logic
        if seconds >= 60:
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)



        colon = ascii_art(":")
        line = ascii_art("│")
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
        display =  line, hour_tens, hour_units, colon, minute_tens, minute_units, colon, second_tens, second_units, line



        # prints the ascii art next to each other

        print("\033[H", end="")
        print(color + "┌" + 62 * "─" + "┐")
        output = ""
        for number in zip(*(number.splitlines() for number in display)):
            output += (color + "".join(number) + "\n")

        output = output.rstrip("\n")
        print(output)
        print(color + "└" + 62 * "─" + "┘")
        # countdown logic and clear screen
        seconds += 1
        time.sleep(1)






application()







# top = "┌" + "─" * (box_width - 2) + "┐"
# bottom = "└" + "─" * (box_width - 2) + "┘"
# middle = "│" + " " * (box_width - 2) + "│"

