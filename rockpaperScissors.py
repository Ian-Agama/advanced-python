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
    #game logic
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

#Chartgpt version

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose again.")
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()