import random

computer_choise = random.choice(["scissors", "rock","paper"])
user_choice = input("Do you want paper, rock  or scissors?\n")
if(computer_choise == user_choice):
    print("TIE")
elif user_choice == "rock" and computer_choise=="scissors":
    print("WIN")
elif user_choice == "paper" and computer_choise=="rock":
    print("WIN")
elif user_choice == "scissors" and computer_choise=="paper":
    print("WIN")
else:
    print("Computer wins")
