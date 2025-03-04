import random  # Import the random module for generating random numbers
import time  # Import time module for delays
import sys  # Import sys for exiting the game

# ANSI color codes for better user experience
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


# Game Introduction
print(CYAN + "\n🎯 Welcome to the Ultimate Number Guessing Game! 🎯" + RESET)
print("Guess a number between 50 and 100.") 
print("Can you guess the correct number? Let's find out!\n")

# Choose difficulty level
print(YELLOW + "Choose your difficulty level:" + RESET)
print("1. Easy (7 attempts)")
print("2. Medium (5 attempts)")
print("3. Hard (3 attempts)")

difficulty = input("Enter 1, 2, or 3: ")

if difficulty == "1":
    max_attempts = 7
elif difficulty == "2":
    max_attempts = 5
elif difficulty == "3":
    max_attempts = 3
else:
    print(RED + "Invalid choice! Defaulting to Medium difficulty." + RESET)
    max_attempts = 5

# Generate a random number between 50 and 100
number_to_guess = random.randint(50, 100)

attempts_taken = 0  # Track attempts
score = 100  # Start score at 100

# Start the game loop
while attempts_taken < max_attempts:
    attempts_taken += 1
    try:
        user_guess = int(input("\n🔢 Enter your guess: "))
    except ValueError:
        print(RED + "❌ Invalid input! Please enter a number." + RESET)
        continue

    # If the guess is correct
    if user_guess == number_to_guess:
        print(GREEN + f"\n🎉 Congratulations! You guessed the number {number_to_guess} in {attempts_taken} attempts!" + RESET)
        print(f"🏆 Your Score: {score} points")
        break
    else:
        # Score penalty
        score -= 10

        # If the player runs out of attempts
        if attempts_taken == max_attempts:
            print(RED + f"\n❌ Oops! You ran out of attempts. The number was {number_to_guess}." + RESET)
            print(f"🏆 Final Score: {score} points")
            break

        # Provide hints
        difference = abs(user_guess - number_to_guess)

        if difference >= 20:
            hint = "❄️ Ice cold!"
        elif difference >= 10:
            hint = "🥶 Cold!"
        elif difference >= 5:
            hint = "🔥 Getting warm!"
        else:
            hint = "🔥🔥 Hot! Almost there!"

        if user_guess > number_to_guess:
            print(YELLOW + f"📉 Too high! {hint} Try again." + RESET)
        else:
            print(YELLOW + f"📈 Too low! {hint} Try again." + RESET)

# Game Over Message
print("\n" + CYAN + "🎮 Thanks for playing! Want to try again? Run the game again!" + RESET)
