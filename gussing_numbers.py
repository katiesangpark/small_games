import random

def guessing_game(level):
    generated_number = random.randint(1, 100)
    attempts_left = 10 if level == "easy" else 5

    while attempts_left > 0:
        print("Guess a number:")
        guess = int(input())
        
        if guess == generated_number:
            print("Congratulations!Congratulations!Congratulations! You guessed the correct number.")
            return
        
        if guess > generated_number:
            print("Too high!")
        else:
            print("Too low!")
        
        attempts_left -= 1
        print("Attempts left:", attempts_left)
    
    print("Game over! You ran out of attempts.")
    print("The correct number was:", generated_number)

# Main program
print("Welcome to the guessing numbers game!")
print("Choose a level: easy or hard")
chosen_level = input()

if chosen_level == "easy" or chosen_level == "hard":
    guessing_game(chosen_level)
else:
    print("Invalid level choice. Please choose either easy or hard.")




# Start
# |
# V
# Print "Welcome to the guessing numbers game!"
# Print "Choose a level: easy or hard"
# Get user's chosen level
# |
# V
# if chosen level is easy or hard:
#     |
#     V
#     Call guessing_game function with chosen level
#     |
#     V
#     End
# else:
#     |
#     V
#     Print "Invalid level choice. Please choose either easy or hard."
#     |
#     V
#     End

# guessing_game function:
# |
# V
# Generate a random number between 1 and 100
# Set attempts_left to 10 if level is easy, otherwise set it to 5
# |
# V
# while attempts_left > 0:
#     |
#     V
#     Print "Guess a number:"
#     Get user's guess
#     |
#     V
#     if guess is correct:
#         |
#         V
#         Print "Congratulations! You guessed the correct number."
#         Return
#     else if guess is too high:
#         |
#         V
#         Print "Too high!"
#     else:
#         |
#         V
#         Print "Too low!"
#     |
#     V
#     Decrease attempts_left by 1
#     Print "Attempts left:", attempts_left
#     |
#     V
# End of while loop
# |
# V
# Print "Game over! You ran out of attempts."
# Print "The correct number was:", generated_number
# |
# V
# End
