#secret auction where people place bids and shows the highest bid at the end.
import os

def clear_terminal():

    os.system("cls" if os.system == "nt" else "clear")






bidders = {}

name = input("What's your name?")
bid = input("What's your bid amount?")

bidders.update({name:bid})

more_people = input("Are there more bidders?")
clear_terminal()

if more_people == "Yes":
    while True:
        name = input("What's your name?")
        bid = input("What's your bid amount?")
        bidders.update({name: bid})

        more_people = input("Are there more bidders?")
        clear_terminal()
        if more_people != "Yes":
                break



highest_bidder = max(bidders.keys())

print(f"{highest_bidder} has won the product with a bid of {bidders[highest_bidder]}!")