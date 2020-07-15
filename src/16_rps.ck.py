import random
# Write a program to play RPS with a user
# Rules
    # rock > scissors
    # scissors > paper
    # paper > rock

# Edge case
    # rock == rock 

# Flow 
# Start up interaction
wins = 0
losses = 0
ties = 0

# create a list of play options
possible_choices = ["rock", "paper", "scissors"]

# assign a random play to the computer using the random module
programs_choice = random.choice(possible_choices)
print(programs_choice)

# User will specify their choice

# Computer makes a choice 
user_choice = input("Choose rock, paper, or scissors: ")

# Both choices are made 

# Compare choices and determine (return) a winner
if user_choice == "rock":
    if programs_choice == "rock":
        #tie
        print("You tied!")
        ties += 1
    elif programs_choice == "paper":
        #prgram wins
        print("You lose!")
        losses += 1
    else:
        # user wins
        print("You won!")
        wins += 1
        
# Keep track of scores

# Allow user to end game 



