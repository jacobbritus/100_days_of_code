from time import sleep



art = """
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠄⠀⠀⠀
⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀
⠀⠀⠀⢠⣿⣇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⣻⣿⣿⣿⣿⡿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣟⣿⣿⣿⣿⣷⣭⠀⠀⠀
⠀⠀⠀⠀⣻⣿⠟⠛⠉⠁⠈⠉⠻⢿⣿⣿⣿⡟⠛⠂⠉⠁⠈⠉⠁⠻⣿⠀⠀⠀
⠀⠀⠀⠀⢾⠀⠀⣠⠄⠻⣆⠀⠈⠠⣻⣿⣟⠁⠀⠀⠲⠛⢦⡀⠀⠠⠁⠀⠀⠀
⠀⠀⠀⠀⢱⣄⡀⠘⠀⠸⠉⠀⠀⢰⣿⣷⣿⠂⢀⠀⠓⡀⠞⠀⢀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⣿⣷⣶⣶⣶⣾⣿⠀⠸⣿⣿⣿⣶⣿⣧⣴⣴⣶⣶⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣏⠇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣟⡿⠂⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠑⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⠀⠀⠈⠿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠄⢻⣿⣿⣿⡗⠀⠀⠀⠀⠈⠀⢨⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡞⠷⠿⠿⠀⠀⠀⠀⢀⣘⣤⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠼⠉⠀⠀⠀⠀⠀⠚⢻⠿⠟⠓⠛⠂⠉⠉⠁⠀⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢾⠻⠌⣄⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⣀⣀⡠⡲⠞⡁⠈⡈⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠘⠛⠻⢯⠟⠩⠀⠀⢠⣣⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⠂⣰⣧⣾⠶⠀⠀⠀⠀⠀⠀⠀
"""

print("You suddenly wake up.")
sleep(2)
print("After what felt like a coma.")
sleep(2)
print("Only to not be able to see anything.")
sleep(2)
print("You try to make sense out of the darkness, but...")
sleep(2)
print("It's too dark.")
sleep(2)

choice = input("\n1. Try to find an exit\n2. Sit down and wait.\n>")
sleep(2)

if choice == "2":
    ...

else:
    print("After hours of walking in the darkness.")
    sleep(2)
    print("You feel something tapping your back.")
    sleep(2)
    print("You stop walking.")
    sleep(2)
    print("You turn around...")
    sleep(2)
    print("A face slowly forms in the darkness.")
    sleep(2)
    print(art)
    print("You died.")
    exit()

print("After hours of waiting,")
sleep(2)
print("You realize that no one is coming to save you.")
sleep(2)
print("So you get up and start looking for a way out.")
sleep(2)
print("Hours pass while walking...")
sleep(2)
print("A light forms in the distance.")
sleep(2)

choice = input("\n1. Walk towards the light.\n2. Avoid the light.\n>")
sleep(2)

if choice == "1":
    ...
else:
    print("After hours of walking in the darkness.")
    sleep(2)
    print("You feel something tapping your back.")
    sleep(2)
    print("You stop walking.")
    sleep(2)
    print("You turn around...")
    sleep(2)
    print("A face slowly forms in the darkness.")
    sleep(2)
    print(art)
    print("You died.")
    exit()



print("As you walk towards the light,")
sleep(2)
print("It becomes brighter and brighter.")
sleep(2)
print("You're now close enough to try to make sense of what the light is emanating from.")
sleep(2)
print("Could there be a human?")
sleep(2)
print("It's seems to be just an abandoned smartphone...")
sleep(2)
print("It suddenly plays a loud ringtone.")
sleep(2)
print("You hear footsteps coming your direction!")


phone = input("\n 1. Pick up the phone.\n2. Run away\n>")
sleep(2)

if phone == "1":
    ...
else:
    print("You decide to run away.")
    sleep(2)
    print("After what feels like hours of running.")
    sleep(2)
    print("You decide to stop running.")
    sleep(2)
    print("You feel something tapping your back.")
    sleep(2)
    print("You turn around...")
    sleep(2)
    print("A face slowly forms in the darkness.")
    sleep(2)
    print(art)
    print("You died.")
    exit()

print("You pick up the phone, turn it off, and run away.")
sleep(2)
print("After minutes of running,")
sleep(2)
print("You stop hearing steps.")
sleep(2)
print("You decide to look into the smartphone.")
sleep(2)
print("You turn it on and see a happy family background.")
sleep(2)
print("The phone is locked.")
sleep(2)
print("The phone starts playing the same loud ringtone again.")
sleep(2)
print("You're being called by \"Unknown\".")
sleep(2)

choice = input("\n 1. Decline.\n2. Accept.\n>")
sleep(2)

if choice == "2":
    ...
else:
    print("You decided to decline the call.")
    sleep(2)
    print("You decide to keep looking for an exit.")
    sleep(2)
    print("After hours of walking in the darkness.")
    sleep(2)
    print("You feel something tapping your back.")
    sleep(2)
    print("You stop walking.")
    sleep(2)
    print("You turn around...")
    sleep(2)
    print("A face slowly forms in the darkness.")
    sleep(2)
    print(art)
    print("You died.")
    exit()

print("You pick up as soon as possible to avoid being chased again.")
sleep(2)
print("You hear a distant voice:")
sleep(2)
print("\"Wake up, wake up, wake up\"")
sleep(2)
print("\"Wake up, wake up, wake up\"")
sleep(2)
print("\"Wake up, wake up, wake up\"")
sleep(2)
print("The phone turns off.")
sleep(2)
print("You feel something tapping your back.")
sleep(2)
print("You turn around...")
sleep(2)
print("A face slowly forms in the darkness.")
sleep(2)
print(art)
sleep(5)
print("It doesn't move...")
sleep(2)
print("It keeps staring at you.")
sleep(2)
print("You're completely frozen and unable to move even an inch.")
sleep(2)
print("It fades back into the darkness again.")
sleep(2)
print("You suddenly feel extremely fatigued.")
sleep(2)
print("You fall asleep.")