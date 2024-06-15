import random
from enum import IntEnum

options = ["rock", "paper", "scissors"]


def get_computer_selection():
    selection = random.choice(options)
    return selection


def determins_winner(user_action:str, computer_action:str)->None:
    if user_action == computer_action:
        print(f'Both users chose {user_action}. Tie!!')
    elif user_action == "scissors":
        if computer_action == "paper":
            print('Scissors cut paper! You win!')
        else:
            print('Rock beats scissors! You lose.')
    elif user_action == "paper":
        if computer_action == "rock":
            print('Paper wraps around a rock! You win!')
        else:
            print('Scissors cut paper! You lost.')
    elif user_action == "rock":
        if computer_action == "scissors":
            print('Rock beats scissors! You win!')
        else:
            print('The paper wraps around the rock! You lose.')


while True:
    user_action = str(input(f"Input your selection:{options}")).lower()

    if user_action in options:
        Zalupa =""
        computer_action = get_computer_selection()
        print(f'\nYou chose {user_action}, The computer has chosen {computer_action}.\n')
        determins_winner(user_action, computer_action)
    else:
        print("IDI NAHUI")
    play_again = input('Сыграем еще? (д/н): ').lower()
    if play_again != 'д':
        break
