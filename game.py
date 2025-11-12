import random  # Import the 'random' module to allow the computer to make a choice

# --- Game Setup ---
# Assign numerical values to the computer's choice: 1=Rock, 0=Paper, -1=Scissor
# 'random.choice' selects one value randomly from the list [-1, 0, 1]
computer = random.choice([-1, 0, 1])

# Prompt the user for input (r for rock, p for paper, s for scissor)
user = input("Enter your choice (r, p, or s): ")

# Dictionary to map user input (r, p, s) to their numerical equivalents
dict = {
    "r": 1,   # Rock is represented by 1
    "p": 0,   # Paper is represented by 0
    "s": -1   # Scissor is represented by -1
}

# Reverse Dictionary to map the numerical values back to human-readable words
revDict = {
    1: "rock",
    0: "paper",
    -1: "scissor"
}

# --- Display Choices ---
# Use the dictionaries to translate and print what the user chose
print(f"you chose {revDict[dict[user]]}")
# Use the reverse dictionary to translate and print what the computer chose
print(f"computer chose {revDict[computer]}")


# --- Game Logic ---
# Check for a draw: if the user's value is the same as the computer's value
if (dict[user] == computer):
    print("match is draw")

# If it's not a draw, check for win or loss conditions
else:
    # Win condition check (User wins):
    # Rock (1) beats Scissor (-1) OR Paper (0) beats Rock (1) OR Scissor (-1) beats Paper (0)
    if (dict[user] == 1 and computer == -1) or (dict[user] == 0 and computer == 1) or (dict[user] == -1 and computer == 0):
        print("you win")

    # Loss condition check (Computer wins, User loses):
    # Scissor (-1) loses to Rock (1) OR Rock (1) loses to Paper (0) OR Paper (0) loses to Scissor (-1)
    elif (dict[user] == -1 and computer == 1) or (dict[user] == 1 and computer == 0) or (dict[user] == 0 and computer == -1):
        print("you lose")

    # Fallback for invalid input (e.g., if the user enters something not in the 'dict' keys)
    # NOTE: A proper program would use a 'try-except' block or a 'while' loop for better error handling here.
    else:
        print("Enter valid choice")
