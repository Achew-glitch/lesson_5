# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельсвует пустая строка.

import os

with open('input_list.txt', 'w') as file_input:
    while True:
        w_str = input('Введите строку: ')
        if w_str == '':
            break
        else:
            file_input.write(w_str + '\n')

print(os.path.realpath('input_list.txt'))