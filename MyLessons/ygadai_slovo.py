from random import *
from time import *


def get_random_word():
    file1 = open("../files/singular.txt", "r", encoding='utf-8')
    words = []
    while True:
        line = file1.readline()
        if not line:
            break
        if 5 <= len(line) <= 7:
            words.append(line[:-1])
    file1.close()

    return choice(words).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ ⎞
                   |    
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ 
                   |
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |
                   |
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼
                   |
                   |
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      ▼
                   |
                   |
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   -
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''  
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                    
                '''
    ]
    return stages[tries]


def play(slovo):
    tries = 10
    print(display_hangman(tries))
    print(f'Давайте играть в угадайку слов!\n'
          f'В загаданном слове {len(slovo)} букв')
    guessed_letters = []
    guessed_words = []
    print('_' * len(slovo))
    errors = len(slovo)
    while True:
        bukva = input('Введите букву или сразу слово: ')
        if len(bukva) == 1 and bukva.isalpha():
            if bukva.upper() not in guessed_letters:
                guessed_letters.append(bukva.upper())
                if bukva.upper() in slovo:
                    print(f'Есть попадание в букву {bukva.upper()} ...')
                    sleep(1)
                    for i in slovo:
                        if i == bukva.upper():
                            errors -= 1
                else:
                    print(f'Мимо...')
                    sleep(1)
                    tries -= 1
            elif bukva.upper() in guessed_letters:
                print('Ты уже называл эту букву!!')
                sleep(1)
                continue

        elif len(bukva) == len(slovo):
            if bukva.upper() not in guessed_words:
                guessed_words.append(bukva.upper())
                if bukva.upper() == slovo:
                    print(f'Гениально!!! Ты не повесился!!... Это действительно {slovo}!')
                    break
                else:
                    tries -= 1
            elif bukva.upper() in guessed_words:
                print('Ты уже называл это слово!!')
                sleep(1)
                continue

        elif len(bukva) > len(slovo):
            print('Слишком длинное слово ты ввел... попробуй снова...')
            sleep(1)
        elif 1 < len(bukva) < len(slovo):
            print('Слишком короткое слово, прямо как твой... попробуй снова...')
            sleep(1)
        else:
            print('Ты ввел чушь...')
            sleep(1)
            continue
        if len(guessed_letters) > 0:
            print('Буквы, которые вы называли: ', end='')
            print(*guessed_letters, sep=',')
        if len(guessed_words) > 0:
            print('Слова, которые вы называли: ', end='')
            print(*guessed_words, sep=',')
        print(display_hangman(tries))
        for i in slovo:
            if i not in guessed_letters:
                print('_', end='')
            elif i in guessed_letters:
                print(i, end='')
        print()
        if errors == 0:
            print(f'Гениально!!! Ты не повесился!!... Это действительно {slovo}!')
            break
        if tries == 0:
            print(f'Эх...додик...додик... Ты повешен...Это было слово {slovo}')
            break

word = get_random_word()
play(word)
