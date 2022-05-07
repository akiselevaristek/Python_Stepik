en_upper = [chr(i) for i in range(65, 91)]
en_lower = [chr(i) for i in range(97, 123)]
rus_upper = [chr(i) for i in range(1072, 1104)]
rus_lower = [chr(i) for i in range(1040, 1072)]


s = input('Введите текст для шифрования: ')
print(s.split())
# n = int(input('Введите сдвиг: '))
v = 'ш'

# while True:
#     v = input('Шифруем или дешифруем? Введите ш или д: ')
#     if v in 'шдШД':
#         break
#     else:
#         print('Не пойдет...')


def right_shift_result(sp):
    if sp.index(i) + 1 + len(elem) <= len(sp):
        return sp[sp.index(i) + len(elem)]
    return sp[sp.index(i) + len(elem) - len(sp)]


def left_shift_result(sp):
    if sp.index(i) - len(elem) >= 0:
        return sp[sp.index(i) - len(elem)]
    return sp[sp.index(i) - len(elem) + len(sp)]


for elem in s.split():
    if v in 'шШ':
        for i in elem:
            if i in en_upper:
                print(right_shift_result(en_upper), end='')
            elif i in en_lower:
                print(right_shift_result(en_lower), end='')
            elif i in rus_upper:
                print(right_shift_result(rus_upper), end='')
            elif i in rus_lower:
                print(right_shift_result(rus_lower), end='')
            elif i == ' ':
                print(' ', end='')
            else:
                print(i, end='')
    elif v in 'дД':
        for i in elem:
            if i in en_upper:
                print(left_shift_result(en_upper), end='')
            elif i in en_lower:
                print(left_shift_result(en_lower), end='')
            elif i in rus_upper:
                print(left_shift_result(rus_upper), end='')
            elif i in rus_lower:
                print(left_shift_result(rus_lower), end='')
            elif i == ' ':
                print(' ', end='')
            else:
                print(i, end='')
    print(' ', end='')
