# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randrange

file_name = "task_5.txt"

with open(file_name, "w", encoding="utf-8") as file:
    nums = [str(randrange(0, 101)) for _ in range(10)]
    file.write(" ".join(nums))

with open(file_name, "r", encoding="utf-8") as file:
    nums = [int(num) for num in file.read().split()]
    print(f"Сумма чисел равна {sum(nums)}")
