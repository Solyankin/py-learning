# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join([" ".join([str(num) for num in line]) for line in self.matrix])

    def __add__(self, other):

        if not len(self.matrix) == len(other.matrix):
            raise ValueError("Размерности матриц должны совпадать")

        result = []
        for i in range(len(self.matrix)):
            line = []

            if not len(self.matrix[i]) == len(other.matrix[i]):
                raise ValueError("Размерности матриц должны совпадать")

            for j in range(len(self.matrix[i])):
                line.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(line)
        return Matrix(result)


matrix_1 = Matrix([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
])

print("Matrix 1")
print(matrix_1)

matrix_2 = Matrix([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])

print("\nMatrix 2")
print(matrix_2)

print("\nMatrix 1 + Matrix 2")
print(matrix_1 + matrix_2)
