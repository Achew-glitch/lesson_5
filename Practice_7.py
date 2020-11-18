import json

with open('list_practice_7.txt', 'r', encoding='utf-8') as file_str:
    ind = 1
    average_profit = 0
    f_list = [{}]

    for line in file_str:
        line = line.strip().split()
        profit = int(line[2]) - int(line[3])

        if profit > 0:
            ind += 1
            average_profit += profit

        f_list[0].update({line[0] : profit})

    f_list.append({'Average profit' : average_profit})
    print(f_list)

with open('list_practice_7.json', 'w') as write_jf:
    json.dump(f_list, write_jf)