import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encode_history_texts = []
encode_shifts = []


def top():
    print(r"""                                                                    .   
                                                                  .o8   
 .ooooo.  ooo. .oo.    .ooooo.  oooo d8b oooo    ooo oo.ooooo.  .o888oo 
d88' `88b `888P"Y88b  d88' `"Y8 `888""8P  `88.  .8'   888' `88b   888   
888ooo888  888   888  888        888       `88..8'    888   888   888   
888    .o  888   888  888   .o8  888        `888'     888   888   888 . 
`Y8bod8P' o888o o888o `Y8bod8P' d888b        .8'      888bod8P'   "888" 
                                         .o..P'       888               
                                         `Y8P'       o888o """)


def menu(message):

    if current_menu == "title_screen":
        print(message)
        print(70 * "─")
        print(f" [1] Encode")
        print(f" [2] Decode")
        # print(f" [3] History")
    elif current_menu == "history_menu":
        print(message)
        print(70 * "─")
        print(f" [1] Encode History")
        print(f" [2] Decode History")

    else:
        print(message)
        print(70 * "─")


def application():
    global current_menu

    current_menu = "title_screen"


    while True:
        top()
        menu("Encode and Decode messages.")
        user_input = input(">   ")
        clear_terminal()

        if user_input == "1":
            current_menu = "enc"
            text = get_text()
            shift = get_shift()
            encode(text, shift)

        elif user_input == "2":
            current_menu = "dec"
            text = get_text()
            shift = get_shift()
            decode(text, shift)

        elif user_input == "3" and encode_history_texts:
            current_menu = "history_menu"


        elif user_input == "1" and current_menu == "history_menu":
            encode_history()



        clear_terminal()
        current_menu = "title_screen"







def get_text():
    top()

    if current_menu == "enc":
        menu("Enter text to encode.")
    else:
        menu("Enter text to decode")

    text = input(">  ")

    if current_menu == "enc":
        encode_history_texts.append(text)

    clear_terminal()
    return text.strip()



def get_shift():
    top()
    menu("Enter a shift amount.")

    shift = int(input(">  "))

    if current_menu == "enc":
        encode_shifts.append(shift)



    clear_terminal()
    return shift






def encode(text_to_encode, shift):

    encoded_text = ""
    for letter in text_to_encode:
        try:
            encoded_text += letters[letters.index(letter) + shift]
        except IndexError:
            encoded_text += letters[letters.index(letter) + shift - len(letters)]

    top()
    menu(f"The text has been encoded to: \"{encoded_text}\".")
    input("Press \"Enter\" to continue.")

    clear_terminal()


def encode_history():
    top()
    menu("Encode History (Press \"Enter\" to return).")

    for index, text in enumerate(encode_history_texts):
        print(f"{text.ljust(20)} - {decode(text, encode_shifts[index])}")

    back = input()

    if back == "":
        clear_terminal()
        return



def decode(text_to_decode, shift):
    decoded_text = ""
    for letter in text_to_decode:
        try:
            decoded_text += letters[letters.index(letter) - shift]
        except IndexError:
            decoded_text += letters[letters.index(letter) - shift - len(letters)]

    if current_menu == "history_menu":
        print(decoded_text)

    else:
        top()
        menu(f"The text has been decoded to: \"{decoded_text}\".")
        input("Press \"Enter\" to continue.")

    clear_terminal()

application()
