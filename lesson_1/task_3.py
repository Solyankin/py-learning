# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = int(input("Введите целое положительное число: "))

if num < 0:
    print("Вы ввели отрицательное число: ")
else:
    num_str = str(num)
    num_double_str = num_str + num_str
    num_triple_str = num_double_str + num_str
    result = num + int(num_double_str) + int(num_triple_str)
    print(f"Результат: {result}")
