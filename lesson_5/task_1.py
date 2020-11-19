#  Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

def append_input_text(file):
    text = input("Введите текс: ")
    if not text == "":
        print(text, file=file)
    return text


with open("task_1.txt", "w", encoding="utf-8") as task_1_file:
    while append_input_text(task_1_file):
        pass
