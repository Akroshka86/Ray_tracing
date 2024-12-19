from vector import Vector

# Класс Color наследует все методы от Vector
class Color(Vector):

    # Создаёт объект Color из строки в формате HEX
    @classmethod
    def from_hex(cls, hexcolor="#000000"):

        # Извлекаем диапазон красного цвета, преобразует 16-ричное число в 10-ричное
        x = int(hexcolor[1:3], 16) / 255.0
        y = int(hexcolor[3:5], 16) / 255.0
        z = int(hexcolor[5:7], 16) / 255.0
        return cls(x, y, z)
