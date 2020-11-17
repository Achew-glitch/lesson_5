# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, поличества слов в каждой строке.

with open('array_list.txt', 'r', encoding='UTF-8') as str_count:
    str_list = str_count.readlines()
    print(f'Содержимое файла:\n{str_list}\nСтрок в файле: {len(str_list)}')
    ind = 1
    for el in str_list:
        print(f'Слов в строке {ind}: {len(el.split(" "))}')
        ind += 1