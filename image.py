from vector import Vector
from PIL import Image as PillowImage


class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, col):
        self.pixels[y][x] = col

    def write_png(self, img_file):
        def to_byte(c):
            return round(max(min(c * 255, 255), 0))

        # Создаём пустое изображение Pillow
        img = PillowImage.new("RGB", (self.width, self.height))
        pixel_data = img.load()

        # Заполняем пиксели
        for y in range(self.height):
            for x in range(self.width):
                color = self.pixels[y][x]
                r, g, b = to_byte(color.x), to_byte(color.y), to_byte(color.z)
                pixel_data[x, y] = (r, g, b)

        # Сохраняем изображение как PNG
        img.save(img_file, "PNG")
