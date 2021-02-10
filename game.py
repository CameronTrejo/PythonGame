import random

possible_choices = ['Rock', 'Paper', 'Scissors']

# User selection -- get info from user

user_selection = input("What is your selection? (Rock, Paper, Scissors): ")
#TODO Validate user selection 
print('You chose', user_selection)

# Computer Selection -- find way for computer to select options
computer_selection = random.choices(possible_choices)
print('Computer chose', str(computer_selection))

# Evaluate the results
# Declar a winner
