from color import Color

# Класс описывает базовый материал, который может быть применён к объекту на сцене
class Material:

    def __init__(
        self,
        color=Color.from_hex("#FFFFFF"),
        ambient=0.05,
        diffuse=1.0,
        specular=1.0,
        reflection=0.5,
    ):
        # Цвет материала
        self.color = color

        # Освещение которое будет распределяться по поверхности
        self.ambient = ambient

        # Диффузное освещение описывает как материал рассеивает свет, чем выше, тем ярче поверхность будет освещаться
        self.diffuse = diffuse

        # Блики, определяет как материал отражает свет от источников света
        self.specular = specular

        # Отражение материала, насколько сильно материал отражает свет, чем выше тем зеркальнее будет материал
        self.reflection = reflection

    def color_at(self, position):
        return self.color


class ChequeredMaterial:

    def __init__(
        self,
        color1=Color.from_hex("#FFFFFF"),
        color2=Color.from_hex("#000000"),
        ambient=0.05,
        diffuse=1.0,
        specular=1.0,
        reflection=0.5,
    ):
        self.color1 = color1
        self.color2 = color2
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    # Метод создает шахматный узор
    def color_at(self, position):
        if int((position.x + 5.0) * 3.0) % 2 == int(position.z * 3.0) % 2:
            return self.color1
        else:
            return self.color2
