import random

def play(x):
    Game_choices = ["rock", "paper", "scissors"]
    computer_choice = ""
    user_choice = ""
    win_user = 0
    win_computer = 0
    while win_user < x and win_computer < x:
        user_choice = input("make your choice: (rock, paper, scissors)")
        computer_choice = random.choice(Game_choices)
        if user_choice == computer_choice:
            print("no winner")
    
        if (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("user win")
            win_user += 1
            print(f"user {win_user}, computer {win_computer}")
        else:
            print("computer win")
            win_computer += 1
            print(f"user {win_user}, computer {win_computer}")

    winner = ""
    if (win_user == x): winner = "You"
    else: winner = "Computer"
    print(f"The end, winner is: {winner}")

rounds = input("Please input how many round do you want to play:")
play(int(rounds))
