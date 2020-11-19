#  Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#  Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#  вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("task_3.txt", "r", encoding="utf-8") as file:
    customers = [line.split() for line in file.readlines()]

    print(f"Сотрудники, имеющие оклад менее 20 тыс.:")
    for name, salary in customers:
        if float(salary) < 20000:
            print(name)

    print()

    salaries = [float(customer[1]) for customer in customers]

    print(f"Средний доход сотрудников: {sum(salaries) / len(salaries)}")
