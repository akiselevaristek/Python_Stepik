from random import *


def is_valid(user_num, user_limit):
    if user_num.isdigit() is True:
        if 1 <= int(user_num) <= user_limit:
            return True
    return False


def ugadaika():
    while True:
        limit = input('Введите лимит: ')
        if limit.isdigit() is False:
            print('Лимит должен быть числовым значением, от 2 до 1.000.000.000')
        else:
            limit = int(limit)
            break

    n = randrange(1, limit + 1)
    counter = 0
    print('Добро пожаловать в числовую угадайку')
    while True:
        x = input('Введите число: ')
        counter += 1
        if is_valid(x, limit) is False:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            x = int(x)
        if x == n:
            print(f'Вы угадали, поздравляем! Количество попыток: {counter}')
            break
        elif x < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif x > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue


while True:
    ugadaika()
    end_game = input('Хотите сыграть еще раз? (Да/Нет): ')
    if end_game.lower() == 'нет':
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
