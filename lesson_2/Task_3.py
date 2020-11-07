# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_index = 0

while True:
    month_index = int(input("Введите порядковый номер месяца от 1 до 12: "))
    if month_index in range(1, 13):
        break

    print("Вы ввели некорректное число, повторите попытку.")

months = [
    "Январь",
    "Февраль",
    "Март",
    "Апрель",
    "Май",
    "Июнь",
    "Июль",
    "Август",
    "Сентябрь",
    "Октябрь",
    "Ноябрь",
    "Декабрь"
]

seasons = {
    "Зима": [11, 0, 1],
    "Весна": [2, 3, 4],
    "Лето": [5, 6, 7],
    "Осень": [8, 9, 10]
}

for season in seasons:
    if month_index - 1 in seasons[season]:
        month = months[month_index - 1]
        print(f"Месяц '{month}' относится к сезону '{season}'")

