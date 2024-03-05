import random

def get_computer_choice():
    """Function to randomly select computer's choice"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Function to determine the winner"""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors Game!")

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chooses {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")
