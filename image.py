from vector import Vector
from PIL import Image as PillowImage

# Класс предназначен для создания изображения, установки его пикселей и записи в файл.
class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    # Метод устанавливает цвет для конкретного пикселя
    def set_pixel(self, x, y, col):
        self.pixels[y][x] = col

    # Сохраняет изображение в формате PNG
    def write_png(self, img_file):

        # Преобразует значение цвета из [0, 1] в [0, 255]
        def to_byte(c):
            return round(max(min(c * 255, 255), 0))

        # Создаём пустое изображение в формате RGB
        img = PillowImage.new("RGB", (self.width, self.height))

        # Возвращает объект, позволяющий напрямую изменять пиксели изображения
        pixel_data = img.load()

        # Заполняем пиксели
        for y in range(self.height):
            for x in range(self.width):
                color = self.pixels[y][x]
                r, g, b = to_byte(color.x), to_byte(color.y), to_byte(color.z)
                pixel_data[x, y] = (r, g, b)

        # Сохраняем изображение как PNG
        img.save(img_file, "PNG")
