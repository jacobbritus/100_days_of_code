import os
from datetime import datetime, timedelta

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


BOX_LENGTH = 82
STREAK_TO_BOX = 20
SPACE_BETWEEN_MARKS = BOX_LENGTH // 10


habits_list = {}

habits_list.update({"Exercise": ["o" + " " * SPACE_BETWEEN_MARKS]* 7})

habits_list.update({"Coding": ["o" + " "* SPACE_BETWEEN_MARKS]* 7})



now = datetime.now()

today = now.strftime("%a")
tomorrow = (now + timedelta(1)).strftime("%a")
third = (now + timedelta(2)).strftime("%a")
fourth = (now + timedelta(3)).strftime("%a")
fifth = (now + timedelta(4)).strftime("%a")
sixth = (now + timedelta(5)).strftime("%a")
seventh = (now + timedelta(6)).strftime("%a")

day_today = now.strftime("%d")
day_tomorrow = (now + timedelta(1)).strftime("%d")
day_third = (now + timedelta(2)).strftime("%d")
day_fourth = (now + timedelta(3)).strftime("%d")
day_fifth = (now + timedelta(4)).strftime("%d")
day_sixth = (now + timedelta(5)).strftime("%d")
day_seventh = (now + timedelta(6)).strftime("%d")

print(day_today)



# display habits
def display():
    global habits_list
    print(f"{" " * (STREAK_TO_BOX - 1)}{today}    {tomorrow}    {third}    {fourth}    {fifth}    {sixth}    {seventh}")
    print("─" * (BOX_LENGTH + 1) + "┐")
    for habit in habits_list:
        print("40x".ljust(STREAK_TO_BOX) + "".join(habits_list[habit]).ljust(BOX_LENGTH - STREAK_TO_BOX)  + "│")  #streak to be added still
        print(habit.ljust(BOX_LENGTH + 1) + "│")
        print( "─" * (BOX_LENGTH + 1) + "┘")



def adding():
    global habits_list

    habit = input("Which habit?")
    day = int(input("What day")) - 1

    habits_list[habit][day] = "x" + " " * SPACE_BETWEEN_MARKS




while True:
    display()
    adding()
    clear_terminal()
