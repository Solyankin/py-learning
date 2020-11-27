# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from abc import ABC, abstractmethod

from json import dumps


class NotEnoughEquipmentError(Exception):

    def __init__(self, department, equipment, count):
        super().__init__(self, self.__str__())
        self.department = department
        self.equipment = equipment
        self.count = count

    def __str__(self):
        return f"Недостачно товара на складе [{self.equipment}, {self.count}]"


class DepartmentNotExistsError(Exception):

    def __init__(self, department):
        super().__init__(self, self.__str__())
        self.department = department

    def __str__(self):
        return f"Отдела '{self.department}' не существует на складе"


class EquipmentNotExistsError(Exception):

    def __init__(self, name):
        super().__init__(self, self.__str__())
        self.name = name

    def __str__(self):
        return f"Неизвестное наименование '{self.name}'"


class Department:

    def __init__(self, name):
        self.name = name
        self.equipments = {}

    def __str__(self):
        return str(self.name)

    def add(self, equipment, count):
        current_count = self.equipments[equipment] if equipment in self.equipments.keys() else 0
        self.equipments[equipment] = current_count + count

    def retrieve(self, equipment, count):
        current_count = self.equipments[equipment] if equipment in self.equipments.keys() else 0

        if count > current_count:
            raise NotEnoughEquipmentError(self, equipment, count)

        self.add(equipment, -count)


class Store:

    def __init__(self):
        self.departments = []

    def add(self, department, equipment, count):
        try:
            department = next(dep for dep in self.departments if dep.name == department)
        except StopIteration:
            department = Department(department)
            self.departments.append(department)

        department.add(equipment, count)

    def retrieve(self, department, equipment, count):
        try:
            department = next(dep for dep in self.departments if dep.name == department)
            department.retrieve(equipment, count)
        except StopIteration:
            raise DepartmentNotExistsError(department)

    def info(self):
        return {dep.name: dep.equipments for dep in self.departments}


class Equipment:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def choose(name):
        equipment = {
            "Принтер": Printer,
            "Сканер": Scanner,
            "Копир": Copier
        }

        if name not in equipment:
            raise EquipmentNotExistsError(name)

        return equipment[name]

    @staticmethod
    def create():
        pass

    @abstractmethod
    def info(self):
        pass


class Printer(Equipment):

    def __init__(self, is_color):
        super().__init__("Принтер")
        self.is_color = is_color

    @staticmethod
    def create():
        return Printer(input(f"Принтер цветной? [Y/N] ").upper() == "Y")


class Scanner(Equipment):

    def __init__(self, dpi):
        super().__init__("Сканер")
        self.dpi = dpi

    @staticmethod
    def create():
        return Scanner(abs(int(input(f"Какой dpi? "))))


# Он же ксерокс))
class Copier(Equipment):

    def __init__(self, copies_per_minute):
        super().__init__("Копир")
        self.copies_per_minute = copies_per_minute

    @staticmethod
    def create():
        return Copier(abs(int(input(f"Как производительность, копий/мин? "))))


class Menu:

    def __init__(self):
        self.items = {
            1: "[1] Информация о товарах на складе",
            2: "[2] Добавить товар",
            3: "[3] Забрать товар",
            4: "[4] Показать меню",
            5: "[5] Выход"
        }

    def __str__(self):
        return "\n".join(self.items.values())


store = Store()
menu = Menu()
menu_item = 3

print(f"{menu}\n")

while True:

    menu_item = input(f"Выберите пункт меню: ")

    if menu_item == "1":
        print("=== Информация о товарах на складе ===")
        print(dumps(store.info(), indent=4, ensure_ascii=False))

    elif menu_item == "2":
        print("=== Добавить товар ===")
        try:
            store.add(
                input("Введите наименование отдела: "),
                Equipment.choose(input("Введите наименование товара: ")).create().name,
                int(input("Введите количество товара: "))
            )
        except Exception as error:
            print(error)
    elif menu_item == "3":
        print("=== Забрать товар ===")
        try:
            store.retrieve(
                input("Введите наименование отдела: "),
                input("Введите наименование товара: "),
                int(input("Введите количество товара: "))
            )
        except Exception as error:
            print(error)
    elif menu_item == "4":
        print("=== Меню ===")
        print(menu)
    elif menu_item == "5":
        print("=== Выход ===")
        break
    else:
        print(f"Неправильно выбран пункт меню [{menu_item}]. Попробуйте снова.\n{menu}\n")
