#creating a simple game of rock paper and scissors 
# we will later create the same function with Object Oriented prigramming annd other advanced 
import random
import time
#basic implementation of the game is complete 
def selection_process():
    #game logic is running properly 
    player = input("Enter a value(rock, paper / scissors):")
    computer = ["rock","paper", "scissors"]
    computer_choice = random.choice(computer)
    player_choice = player.lower()
    print(f"{computer_choice}:{player_choice}")

    time.sleep(15)#adds some time and suspence for the program to run 
    if (computer_choice == player_choice):
        return "its a tie!... try again" 
    elif (computer_choice== "paper" and player_choice== "rock"):
        return "its a win... computer wins!"
    elif (computer_choice == "scissors" and player_choice == "paper"):
        return "its a win... computer wins!"
    elif (computer_choice == "rock" and player_choice == "scissors"):
        return "its a win... computer wins!" 
    else:
        return "computer loses.. You win!!!!!"
    
print(selection_process())