
# Представляет собой луч, который является полулинией с начальной точкой и направлением.
class Ray:

    def __init__(self, origin, direction):

        # Точка начала луча
        self.origin = origin

        # Вектор который определяет направление луча
        self.direction = direction.normalize()
