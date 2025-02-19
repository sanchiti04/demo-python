import random

def virtual_dice_game():
    print("🎲 Welcome to the Virtual Dice Roller! 🎲")
    print("Type 'roll' to roll the dice or 'quit' to exit.")
    
    while True:
        command = input("Your choice (roll/quit): ").lower()
        
        if command == "roll":
            dice_number = random.randint(1, 6)
            print(f"🎲 You rolled a {dice_number}!")
        elif command == "quit":
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Invalid command. Type 'roll' or 'quit'.")

virtual_dice_game()
