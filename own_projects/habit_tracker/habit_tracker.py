import os
from datetime import datetime, timedelta
from colorama import Fore, init
init(autoreset=True)
import random

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
def logo():
    print(r""" _         _   _           
| |__  ___| |_| |_ ___ _ _ 
| '_ \/ -_)  _|  _/ -_) '_|
|_.__/\___|\__|\__\___|_|  
""")
BOX_LENGTH = 82
STREAK_TO_BOX = 20
SPACE_BETWEEN_MARKS = 6


habits_list = {}








now = datetime.now()

# print the number of the week day - 1 (starts on sunday), e.g. friday = 4
weekdaynow = now.weekday()

# today's date - the number of the week, to get the week's monday as a datetime object
monday = now - timedelta(weekdaynow)


# adds the whole week in a list as datetime objects
week_in_datetime = [monday + timedelta(i) for i in range(7)]

#prints everything in the week's day's number (01) and day (monday).
week_numbers_display = [Fore.LIGHTBLACK_EX + day.strftime("%d") + Fore.RESET if not day.weekday() == now.weekday() else Fore.WHITE + day.strftime("%d") + Fore.RESET for day in week_in_datetime]
# week_days = [day.strftime("%a") for day in week_in_datetime]

week_days_display = [Fore.LIGHTBLACK_EX + day.strftime("%a") + Fore.RESET if not day.weekday() == now.weekday() else Fore.WHITE + day.strftime("%a") + Fore.RESET for day in week_in_datetime]


# print("  ".join(week_numbers_display))
# print(" ".join(week_days_display))

# when saving is added:
# if day_date(TURN TO FULL DATE TO ALSO CHECK IF EQUAL MONTH AND YEAR) in [d.date() for d in habits_list[habit]["marked_dates"]
# if yes make get it's index and then  habits_list[habit]["marks"][day_date_index] = Fore.GREEN + "[X]" + Fore.RESET + " " * SPACE_BETWEEN_MARKS
# either get the index from list or from turning it into .weekday

# display habits
def display():
    global habits_list

    if habits_list:
        # print("┌" + "─" * (BOX_LENGTH + 1) + "┐")
        # print(f"│{now.strftime("%B").ljust(STREAK_TO_BOX)}{"       ".join(week_numbers_display).ljust(BOX_LENGTH + 15 - STREAK_TO_BOX)}       │")
        # print(f"│{" ".ljust(STREAK_TO_BOX)}{"      ".join(week_days_display).ljust(BOX_LENGTH + 15 - STREAK_TO_BOX)}      │")
        # print("└" + "─" * (BOX_LENGTH + 1) + "┘")
        print(f"{now.strftime("%B").ljust(STREAK_TO_BOX)}{"        ".join(week_numbers_display).ljust(BOX_LENGTH + 15 - STREAK_TO_BOX)}       ")
        print(f"{" ".ljust(STREAK_TO_BOX)}{"       ".join(week_days_display).ljust(BOX_LENGTH + 15 - STREAK_TO_BOX)}      ")


        for index, habit in enumerate(habits_list):
            print("┌" + "─" * (BOX_LENGTH + 1) + "┐")
            print("│" + str(habits_list[habit]["streak"]).ljust(STREAK_TO_BOX) + "".join(habits_list[habit]["marks"]).ljust(BOX_LENGTH - STREAK_TO_BOX)  + "│")  #streak to be added still
            print("│" + habit.ljust(BOX_LENGTH + 1) + "│")
            print("└" + "─" * (BOX_LENGTH + 1) + "┘")

# adding new habits
def adding_habits():
    global habits_list

    print("Enter the new habit's name")
    habit = input("> ")

    habits_list.update({habit: {"marks": ["[O]" + " " * SPACE_BETWEEN_MARKS] * 7,"streak": 0,"marked_dates": []}})

# logging habits
def logging():
    global habits_list

    habit = input("Which habit?")
    day = now.weekday()


    habits_list[habit]["marks"][day] = Fore.GREEN + "[X]" + Fore.RESET + " " * SPACE_BETWEEN_MARKS
    habits_list[habit]["streak"] += 1
    habits_list[habit]["marked_dates"].append(now)

#menu
def menu(message):


    print(message)
    print("┌" + "─" * (BOX_LENGTH + 1) + "┐")
    print(f"│ [1] Log{" " * 59}[3] Edit Habits │")
    print(f"│ [2] New Habit{" " * 53}[4] Settings    │")
    print("└" + "─" * (BOX_LENGTH + 1) + "┘")






def random_quote():
    quotes = ["“Amateurs sit and wait for inspiration, the rest of us just get up and go to work.” — Stephen King",

              "“Don’t watch the clock; do what it does. Keep going.” — Sam Levenson",

              "“Productivity is never an accident. It is always the result of a commitment to excellence, intelligent planning, and focused effort.” — Paul J. Meyer",

              "“The way to get started is to quit talking and begin doing.” — Walt Disney",

              "“Focus on being productive instead of busy.” — Tim Ferriss",

              "“You don’t have to be extreme, just consistent.” — Unknown",

              "“It’s not always that we need to do more but rather that we need to focus on less.” — Nathan W. Morris",

              "“Your future is created by what you do today, not tomorrow.” — Robert Kiyosaki",

              "“Ordinary people think merely of spending time, great people think of using it.” — Arthur Schopenhauer",

              "“Action is the foundational key to all success.” — Pablo Picasso",

              "“Lost time is never found again.” — Benjamin Franklin",

              "“Small daily improvements over time lead to stunning results.” — Robin Sharma",

              "“What gets measured gets managed.” — Peter Drucker",

              "“Start where you are. Use what you have. Do what you can.” — Arthur Ashe",

              "“Nothing will work unless you do.” — Maya Angelou",

              "“Success is the sum of small efforts repeated day in and day out.” — Robert Collier",

              "“The secret of getting ahead is getting started.” — Mark Twain",

              "“Never mistake motion for action.” — Ernest Hemingway",

              "“Simplicity boils down to two steps: Identify the essential. Eliminate the rest.” — Leo Babauta",

              "“Dream big. Start small. Act now.” — Robin Sharma"]

    print(random.choice(quotes))


def main():
    global current_menu

    current_menu = "main_menu"

    while True:
        logo()
        menu(random_quote())
        display()
        get_user_input()
        clear_terminal()



        clear_terminal()



def get_user_input():

    user_input = input("> ")

    if user_input == "1":
        logging()
    elif user_input == "2":
        adding_habits()
    elif user_input == "3":
        ...#
    elif user_input == "4":
        ...
    else:
        input("Invalid input (Press \"Enter\" to continue.")
















main()