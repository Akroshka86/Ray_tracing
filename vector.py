import math


# Этот класс предоставляет основные операции с векторами, необходимые для 3D-графики:
class Vector:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    # Метод для вычисления скалярного произведения между векторами
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Метод для вычисления длины вектора
    def magnitude(self):
        return math.sqrt(self.dot_product(self))

    # Метод для нормализации вектора (показывает куда направлен вектор)
    def normalize(self):
        return self / self.magnitude()

    # Метод для сложения векторов
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # Метод для вычитания векторов
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # Умножение вектора на число
    def __mul__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    # Обратное умножение вектора на число
    def __rmul__(self, other):
        return self.__mul__(other)

    # Деление вектора на число
    def __truediv__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x / other, self.y / other, self.z / other)
