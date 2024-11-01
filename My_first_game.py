
import random

def player():
    player_1 = int(input('Выберите число своего броска (1 - камень, 2 - бумага, 3 - ножницы): '))
    if player_1 in [1, 2, 3]:
        choices = {1: 'камень', 2: 'бумага', 3: 'ножницы'}
        print(player_1, '- вы выбрали', choices[player_1])
        return player_1
    else:
        print('Ошибка: введите число от 1 до 3.')
        return None

def generate_comp():
    computer = random.randint(1, 3)
    choices = {1: 'камень', 2: 'бумага', 3: 'ножницы'}
    print(computer, '- компьютер выбрал', choices[computer])
    return computer

def play(player_choice, computer_choice):
    if player_choice == computer_choice:
        print('Ничья')
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        print('Игрок победил')
    else:
        print('Компьютер победил')

if __name__ == '__main__':
    while True:
        player_choice = player()
        if player_choice is not None:
            computer_choice = generate_comp()
            play(player_choice, computer_choice)

        play_again = input('Хотите сыграть снова? (да/нет): ').strip().lower()
        if play_again != 'да':
            print('Спасибо за игру!')
            break





