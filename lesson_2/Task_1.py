# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


type_list = [
    0,
    0.1,
    complex(1, 2),
    float(0.3),
    "string",
    list("list"),
    tuple("tuple"),
    set("set"),
    frozenset("frozenset"),
    {"k_1": 'v_1', "k2": "v_2"},
    True,
    b'text',
    bytearray(b"some text"),
    None,
    ZeroDivisionError()
]

for item in type_list:
    print(type(item))
