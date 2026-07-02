import random

options = ('paper', 'rock', 'scissors')

computer = random.choice(options)
player = input("Enter choice (rock/paper/scissors): ")

print(f"Player choice: {player}")
print(f"Computer choice: {computer}")

if player == computer:
    print("It's a tie!")

elif player == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose!")

elif player == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("You lose!")

elif player == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("You lose!")

else:
    print("Invalid input")