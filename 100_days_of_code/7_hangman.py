import random
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")









def top(show):

    if show == "logo":
        print(r"""┌─────────────────────────────────────────────────────────┐
│      _   _                                              │
│     | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __       │
│     | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \      │
│     |  _  | (_| | | | | (_| | | | | | | (_| | | | |     │
│     |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     │     
│                        |___/                            │
├─────────────────────────────────────────────────────────┤""")

    else:

        print(f"""┌─────────────────────────────────────────────────────────┐
│                                                         │
│                                                         │
│{"".join(show).center(57)}│ 
│                                                         │
│                                                         │     
│                                                         │
├─────────────────────────────────────────────────────────┤""")




def main():
    global current_menu
    current_menu = "main_menu"

    game_result = ""
    hidden_letters = ""
    while True:
        if not game_result == "":
            top(hidden_letters)
            menu(None, game_result)
        else:
            top("logo")
            menu("", "")
        user_input = input("> ")
        clear_terminal()

        if current_menu == "main_menu":
            if user_input == "1":
                current_menu = "pre_game_menu"
            elif user_input == "2":
                exit()
            else:
                input("Invalid input - (Enter [1] or [2])")
        elif current_menu == "pre_game_menu":
            if user_input == "1":
                current_menu = "guessing_menu"
                game_result = game("easy")


            elif user_input == "2":
                current_menu = "guessing_menu"
                hidden_letters, game_result = game("medium")


            elif user_input == "3":
                current_menu = "guessing_menu"
                game_result = game("hard")

            elif user_input == "4":
                current_menu = "main_menu"
            else:
                input("Invalid input")
        elif current_menu == "post_game_menu":

            if user_input == "1":
                current_menu = "pre_game_menu"
            elif user_input == "2":
                current_menu = "main_menu"


def menu(lives, message):

    if current_menu == "main_menu":
        print(f"│Main Menu {" " * 47}│")
        print("├" + 57 * "─" + "┤")
        print(f"│ [1] Start{" " * 47}│")
        print(f"│ [2] Exit{" " * 48}│")
        print("└" + 57 * "─" + "┘")
    elif current_menu == "pre_game_menu":
        print(f"│< Main Menu {" " * 45}│")
        print("├" + 57 * "─" + "┤")
        print(f"│ [1] Easy{" " * 48}│")
        print(f"│ [2] Medium{" " * 46}│")
        print(f"│ [3] Hard{" " * 48}│")
        print(f"│ [4] Back{" " * 48}│")
        print("└" + 57 * "─" + "┘")
    elif current_menu == "guessing_menu":
        print(f"│ {message}{" "  * (56 - len(message) if message else 56)}│")
        print("├" + 57 * "─" + "┤")
        print(f"│ Guess a letter.{" " * 41}│")
        print(f"│ You have: {lives} left {" "  * (39 - len(str(lives)))} │")
        print("└" + 57 * "─" + "┘")
    elif current_menu == "post_game_menu":
        print(f"│ {message}{" "  * (56 - len(message) if message else 56)}│")
        print("├" + 57 * "─" + "┤")
        print(f"│ [1] Play Again{" " * 42}│")
        print(f"│ [2] Back{" " * 48}│")
        print("└" + 57 * "─" + "┘")


def game(difficulty): #difficulty parameter set through game menu
    global current_menu
    if difficulty == "easy":
        word_list = ["cat", "dog", "sun", "tree", "car"]
        hint_list = ["annoying pet", "loyal pet", "the big star", "tall and green", "vroom vroom"]
    elif difficulty == "hard":
        word_list = ["window", "planet", "bottle", "python", "guitar"]
    else:
        word_list = ["astronaut", "kaleidoscope", "algorithm", "labyrinth", "encylopedia"]

    #3 lists each with their own difficulty


    word_to_guess = random.choice(word_list) # random.choice()


    # hint = hint_list[word_list.index(word_to_guess)]

    hidden_letters = []

    hidden_letters += "_" * len(word_to_guess)

    lifes: int = 10

    sysmessage = "Good luck"
    while "".join(hidden_letters) != word_to_guess and not lifes == 0:
        top(hidden_letters)
        menu(lifes, sysmessage)



        guessed_letter = input("> ")
        if guessed_letter == "":
            ...

        elif guessed_letter in "".join(hidden_letters) and guessed_letter in word_to_guess:
            sysmessage = f"You already guessed \"{guessed_letter}\" right."


        elif guessed_letter in word_to_guess:
            for index, letter in enumerate(word_to_guess):
                if letter == guessed_letter:
                    hidden_letters[index] = guessed_letter

            sysmessage = f"\"{guessed_letter}\" is in the word. Good job."



        elif guessed_letter not in word_to_guess:
            lifes -= 1

            if lifes > 5:
                sysmessage = f"\"{guessed_letter}\" is not in the word. Try again."
            # else:
            #     sysmessage = f"\"{guessed_letter}\" is not in the word. Here's a hint: {hint}."



        clear_terminal()

        #elif guessed_letter == hint
        #sysmessage = ...
    current_menu = "post_game_menu"
    return hidden_letters, "You guessed \"{word_to_guess}\" right! You had {lifes} Lives left."









main()


