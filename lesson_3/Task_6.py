# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

# Фраза для проверки:
# nice авп ъghj jапро hjjпаро вапрghgh cool -> Nice Cool

def int_func(txt):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in txt.lower():
        if i not in alphabet:
            return ""

    return txt.title()


text = input("Введите строку, состоящую из слов, разделенных пробелом: ").split()
words = []

for word in text:
    w = int_func(word)
    if w != "":
        words.append(w)

print(" ".join(words))
