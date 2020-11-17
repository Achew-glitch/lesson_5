rus_list = ['Один', 'Два', 'Три', 'Четыре']

with open('list_practice_4.txt', 'r', encoding='utf=8') as str_list:
    for ind in range(len(rus_list)):
        rus_list[ind] = rus_list[ind] + ' - ' + str_list.readline().strip().split(' - ')[1] + '\n'

with open('new_list_practice_4.txt', 'w', encoding='utf-8') as w_line:
    w_line.writelines(rus_list)
