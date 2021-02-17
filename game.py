import random

possible_choices = ['Rock', 'Paper', 'Scissors']

# loop through the code until user wants to quit
while True:
    
    # User selection -- get info from user

    user_selection = input("What is your selection? (Rock, Paper, Scissors): ") #TODO Validate user selection 
    print('You chose', user_selection)

    # Computer Selection -- find way for computer to select options
    computer_selection = random.choice(possible_choices)
    
    print('Computer chose', str(computer_selection))

    # Evaluate the results -- Conditional statement
    if user_selection == computer_selection:
        print("It is a tie")

    #----------ROCK----------
    elif user_selection == "Rock":
        #computer selects paper
        if computer_selection == "Paper":
            print("User loses")
        #computer selects scissors
        else:
            print("User wins")

    #----------PAPER----------
    elif user_selection == "Paper":
        if computer_selection == "Scissors":
            print("User loses")
        else:
            print("User wins")

    #----------SCISSORS----------
    elif user_selection == "Scissors":
        if computer_selection == "Rock":
            print("User loses")
        else:
            print("User wins")

    # Declare a winner

    play_again = input("Do you want to play again (y/n): ")
    if play_again == "n":
        break
        #break out of the loop

# This is outside of the loop
print("Thanks for playing!")
