rock = """
    _______              
---'   ____)        
      (_____)                  
      (_____)                  
      (____)           
---.__(___)        
ROCK                

"""

paper = """
    _______                    
---'   ____)____            
           ______)                    
           _______)                 
         _______)                  
---.__________)             
PAPER                      

"""

scissor = """
    _______
---'   ____)____
           ______)
       __________)
      (____)
---.__(___)
Scissors
"""


import random
choices = [rock, paper, scissor]


choice = int(input("0.Rock\n1.Paper\n2.Scissors\n>"))

print("You")
print(choices[choice])


computer_choice = random.randint(0, 2)

print("Computer:")
print(choices[computer_choice])

if choice == 0 and computer_choice == 0:
    print("It's a draw!")
elif choice == 0 and computer_choice == 1:
    print("You lost!")
elif choice == 0 and computer_choice == 2:
    print("You won!")

elif choice == 1 and computer_choice == 0:
    print("You won!")
elif choice == 1 and computer_choice == 1:
    print("It's a draw!")
elif choice == 1 and computer_choice == 2:
    print("You lost!")

elif choice == 2 and computer_choice == 0:
    print("You lost!")
elif choice == 2 and computer_choice == 1:
    print("It's a won!")
elif choice == 2 and computer_choice == 2:
    print("It's a draw!")

else:
    print("Invalid input")