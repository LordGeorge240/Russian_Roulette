import os
import time
import random

def typing_effect(text, delay=0.1):
    """Simulates typing effect letter by letter with a small delay between each letter."""
    for line in text.split("\n"):  # Split the monologue into lines
        for char in line:  # For each character in the line
            print(char, end='', flush=True)  # Print each character on the same line
            time.sleep(delay)  # Pause for a moment after each character
        print()  # After finishing a line, move to the next line

# Game introduction
monologue = """\033[3mWelcome to Russian Roulette.

You have chosen to test your luck—but you're not alone.

This is a game of fate, and both of us will take turns.

Will fortune favor you, or will I be the last one standing?

Only one way to find out...\033[0m"""
typing_effect(monologue)

# Game loop
while True:
    # Player's turn
    user_input = input("\nPress Enter to pull the trigger...")
    if user_input == "":  # If ENTER is pressed without typing anything
        bullet_position = random.randint(1, 6)  # 1/6 chance to lose
        if bullet_position == 1:
            typing_effect("\nBANG! You didn't make it...\nGame Over.", delay=0.1)
            os.system("shutdown /s /t 1")  # Windows shutdown (change for Linux/Mac)
            break

        typing_effect("\nClick! \033[3mYou survived... Now it's my turn.\033[0m", delay=0.1)

        # Computer's turn
        bullet_position = random.randint(1, 6)
        if bullet_position == 1:
            typing_effect("\nBANG! Your opponent lost.", delay=0.1)
            break

        typing_effect("\nClick! \033[3mSeems like I survived... Now it's your turn.\033[0m", delay=0.1)
    else:
        print("You must press ENTER to continue...")  # Notify user if they don't press ENTER
