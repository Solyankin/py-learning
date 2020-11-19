# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке

with open("task_2.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(f"Количество строк: {len(lines)}")

    for index, words in enumerate([line.split() for line in lines]):
        print(f"В строке #{index} количество слов равно {len(words)}")
