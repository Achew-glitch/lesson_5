with open('list_practice_3.txt', 'r', encoding='utf=8') as str_list:
    str_list = str_list.readlines()
    print(f'Содержимое файла:\n{str_list}')

avarge_pay = 0
for el in str_list:
    el = el.strip().split(' ')
    if int(el[1]) < 450000:
        print(f'{el[0]} имеет зарплату меньше 450 000')

    avarge_pay += int(el[1])
print(f'Средная зарплата сотрудников: {avarge_pay / len(str_list)}')