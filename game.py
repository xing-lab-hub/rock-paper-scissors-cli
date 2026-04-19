import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if player_choice == 'quit':
            print(f"\nFinal Score - You: {player_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break
            
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if "You win" in result:
            player_score += 1
        elif "Computer wins" in result:
            computer_score += 1

if __name__ == "__main__":
    play_game()
