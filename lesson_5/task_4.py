# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


num_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}


with open("task_4.txt", "r", encoding="utf-8") as file:
    text = file.read()
    text_new = text

    for key in num_dict.keys():
        text_new = text_new.replace(key, num_dict[key])

    with open("task_4_new.txt", "w", encoding="utf-8") as file_new:
        file_new.write(text_new)




