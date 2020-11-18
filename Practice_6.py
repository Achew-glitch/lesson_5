academic_disciplines = {}

with open('list_practice_6.txt', 'r', encoding='utf-8') as file_str:
    for s_el in file_str.readlines():
        s_el = s_el.strip().split()
        time_summary = 0

        for i_el in s_el:
            if i_el == '-' or i_el[len(i_el) - 1] == ':':
                continue
            else:
                time_summary += int(i_el.split('(')[0])

        academic_disciplines.update({s_el[0][:-1] : time_summary})
        print(academic_disciplines)
