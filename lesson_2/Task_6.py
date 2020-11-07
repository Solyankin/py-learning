# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

menu = {
    "Добавить товар": "1",
    "Посмотреть структуру": "2",
    "Посмотреть аналитику": "3",
    "Завершить работу": "4",
    "Показать меню": "5"
}

# Вынес наименование ключей структуры
name_key = "наименование"
cost_key = "цена"
count_key = "количество"
measure_key = "eд"

# Добавил товаров для простоты отладки
goods = [
    (1, {name_key: "компьютер", cost_key: 20000, count_key: 5, measure_key: "шт."}),
    (2, {name_key: "принтер", cost_key: 6000, count_key: 2, measure_key: "шт."}),
    (3, {name_key: "сканер", cost_key: 2000, count_key: 7, measure_key: "шт."})
]

menu_item = "5"

while menu_item not in menu.values() or menu_item != "4":

    if menu_item == "5":
        print()
        for item in menu:
            print(f"{menu[item]}: {item}: ")

    menu_item = input("\nВыберите пункт меню: ")

    if menu_item == "1":
        name = input("Введите наименование товара: ")
        cost = round(float(input("Введите цену товара: ")), 2)
        count = round(float(input("Введите количество товара: ")), 6) # float, т.к. могут быть кг, м и т.д.
        measure = input("Введите единицу измерения товара: ")
        goods.append(
            (
                len(goods),
                {
                    name_key: name,
                    cost_key: cost,
                    count_key: count,
                    measure_key: measure
                }
            )
        )
    elif menu_item == "2":
        for item in goods:
            print(item)
    elif menu_item == "3":

        name_list = []
        cost_list = []
        count_list = []
        measure_list = []

        for item in goods:
            item_desc = item[1]
            name_list.append(item_desc[name_key])
            cost_list.append(item_desc[cost_key])
            count_list.append(item_desc[count_key])
            measure_list.append(item_desc[measure_key])

        analytics = {
            name_key: name_list,
            cost_key: cost_list,
            count_key: count_list,
            measure_key: measure_list
        }

        for key in analytics:
            print(f"{key:15}: {analytics[key]}")

