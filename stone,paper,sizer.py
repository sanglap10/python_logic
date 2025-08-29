import random

def game():
    while True:
        print("Start rock, paper, scissor game!")
        choices=['rock','paper','scissor']

        user_choice = input("Enter choice: ").lower()
        

        if user_choice == "quit":
            break

        if user_choice not in choices:
            print("INVALID")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer choose: {computer_choice}")

        if computer_choice == user_choice:
            print("Draw")
        elif computer_choice == 'rock' and user_choice == 'scissor':
            print("Computer won")
        elif computer_choice == 'paper' and user_choice == 'rock':
            print("Computwer won")
        elif computer_choice == 'scissor' and user_choice == 'paper':
            print("Computer won")
        else:
            print("You won")

game()