with open('list_practice_5.txt', 'w') as file_input:
    file_input.write(input('Введите числа: ') + '\n')

with open('list_practice_5.txt', 'r') as file_input:
    file_input = file_input.readline().split()
    print(sum(map(int, file_input)))