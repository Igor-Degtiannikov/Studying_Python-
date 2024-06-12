import random
from enum import IntEnum

options = ["rock", "paper", "scissors"]


def get_computer_selection():
    selection = random.choice(options)
    return selection


def determins_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f'Оба пользователя выбрали {user_action.name}. Ничья!!')
    elif user_action == "scissors":
        if computer_action == "paper":
            print('Ножницы режут бумагу! Вы победили!')
        else:
            print('Камень бьет ножницы! Вы проиграли.')
    elif user_action == "paper":
        if computer_action == "rock":
            print('Бумага оборачивает камень! Вы победили!')
        else:
            print('Ножницы режут бумагу! Вы проиграли.')
    elif user_action == "rock":
        if computer_action == "scissors":
            print('Камень бьет ножницы! Вы победили!')
        else:
            print('Бумага оборачивает камень! вы проиграли.')


while True:
    user_action = str(input(f"Input your selection:{options}")).lower()

    if user_action in options:

        computer_action = get_computer_selection()
        print(f'\nВы выбрали {user_action}, Компьютер выбрал {computer_action}.\n')
        determins_winner(user_action, computer_action)
    else:
        print("IDI NAHUI")
    play_again = input('Сыграем еще? (д/н): ').lower()
    if play_again != 'д':
        break
