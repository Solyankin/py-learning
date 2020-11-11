# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

exit_symbol = 'q'
result = 0

while True:
    in_value = input(f"Введите числа, разделеные пробелом, либо '{exit_symbol}/{exit_symbol.upper()}' для выхода: ")

    if in_value.lower().strip() == exit_symbol:
        print(f"Итоговая сумма: {result}")
        break

    pre_result = result
    values = in_value.split()

    error = False

    for i in range(len(values)):
        try:
            result += float(values[i])
        except ValueError:
            error = True
            print(f"Введенное значение [{values[i]}] не является числом.")
            break

    if not error:
        print(f"{result} ({pre_result})")


