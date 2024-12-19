from color import Color

# Представляет точечный источник света, который используется для освещения объектов на сцене.
class Light:

    def __init__(self, position, color=Color.from_hex("#FFFFFF")):
        self.position = position
        self.color = color
