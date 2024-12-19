from image import Image
from ray import Ray
from point import Point
from color import Color


# Класс реализует основной процесс трассировки лучей
class RenderEngine:

    # Мксимальное число рекурсий
    MAX_DEPTH = 5

    # Смещение вторичного луча
    MIN_DISPLACE = 0.001

    # Метод отвечает за рендер всей сцены
    def render(self, scene):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height

        # Установка размер виртуального экрана (экран размерами от -1 до +1)
        x0 = -1.0
        x1 = +1.0
        xstep = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspect_ratio
        y1 = +1.0 / aspect_ratio
        ystep = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        # Цикл по всем пикселям изображения
        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep

                # Создание луча (начальная точка - камера, направление в точку (x, y))
                ray = Ray(camera, Point(x, y) - camera)

                # Установка полученного цвета с помощью метода ray_trace к пикселю (i, j)
                pixels.set_pixel(i, j, self.ray_trace(ray, scene))
            print("{:3.0f}%".format(float(j) / float(height) * 100), end="\r")
        return pixels

    # Метод реализующий трассировку лучей
    def ray_trace(self, ray, scene, depth=0):

        # Инициализация базового цвета
        color = Color(
            0,
            0,
            0,
        )

        # Метод find_nearest находит ближайший объект с которым пересекается луч, если такого нет, то возвращается черный цвет.
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return color

        # Вычисляется точка пересечния луча с объектом
        hit_pos = ray.origin + ray.direction * dist_hit

        # Вычисляется нормаль поверхности объекта в точке пересечения
        hit_normal = obj_hit.normal(hit_pos)

        # Вычисление цвета объекта в точке пересечения
        color += self.color_at(obj_hit, hit_pos, hit_normal, scene)

        # Рекурсивная обработка изображения
        if depth < self.MAX_DEPTH:

            # Начало нового луча перемещается вдоль нормали
            new_ray_pos = hit_pos + hit_normal * self.MIN_DISPLACE

            # Вычисляется направление нового луча
            new_ray_dir = (
                ray.direction - 2 * ray.direction.dot_product(hit_normal) * hit_normal
            )

            # Создается новый луч
            new_ray = Ray(new_ray_pos, new_ray_dir)

            # Метод вызывается для нового луча (умнажаем, чтобы симулировать реальное отражение цвета от объекта)
            color += (
                self.ray_trace(new_ray, scene, depth + 1) * obj_hit.material.reflection
            )
        return color

    # Метод ищет ближайший объект на сцене с которым пересекается луч
    def find_nearest(self, ray, scene):

        # Расстояние от н.т. луча до точки пересечения
        dist_min = None

        # объект с которым произошло пересечение
        obj_hit = None

        # Цикл перебирает все объекты на сцене
        for obj in scene.objects:

            # Метод возвращает расстояние до точки пересечения
            dist = obj.intersects(ray)

            # если произошло пересечение, то обновляем dist_min и obj_hit
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj
        return (dist_min, obj_hit)

    # Метод вычисляет цвет в точке пересечения луча с объектом
    def color_at(self, obj_hit, hit_pos, normal, scene):

        # Получение материала и цвета объекта
        material = obj_hit.material
        obj_color = material.color_at(hit_pos)

        # Вычисляется вектор от точки пересечения до камеры (используется для зеркальных отражений)
        to_cam = scene.camera - hit_pos

        # Резкость блика, чем выше, тем меньше площадь, но ярче блик
        specular_k = 50

        # Создание окружающего белого света, дабы придать цвета объектам на который не падает свет
        color = material.ambient * Color.from_hex("#FFFFFF")

        # Обработка каждого источника света
        for light in scene.lights:

            # Создается луч от точки пересечения до источника света
            to_light = Ray(hit_pos, light.position - hit_pos)

            # Диффузное освещение (Ламберт)
            # normal.dot_product(to_light.direction) - вычисляется косинус угла между нормалью и направлением источника света
            color += (
                obj_color
                * material.diffuse
                * max(normal.dot_product(to_light.direction), 0)
            )

            # Зеркальное освещение
            half_vector = (to_light.direction + to_cam).normalize()
            color += (
                light.color
                * material.specular
                * max(normal.dot_product(half_vector), 0) ** specular_k
            )
        return color
