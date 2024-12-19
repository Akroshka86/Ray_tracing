from math import sqrt


class Sphere:

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    # Метод определяет пересекает ли заданный луч сферу
    def intersects(self, ray):

        # sphere_to_ray - вектор от центра сферы до начальной точки луча
        sphere_to_ray = ray.origin - self.center

        # b - коэффициент в квадратном уравнении пересечения.
        b = 2 * ray.direction.dot_product(sphere_to_ray)

        # c — свободный член квадратного уравнения.
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius

        # Вычисление дискриминанта
        discriminant = b * b - 4 * c

        # Если discriminant >= 0, то есть пересечение
        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None

    # Метод вычисляет нормаль (перпендикуляр) к поверхности сферы в заданной точке
    def normal(self, surface_point):
        return (surface_point - self.center).normalize()
