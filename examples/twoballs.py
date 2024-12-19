from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from light import Light
from material import Material, ChequeredMaterial

# Задаем размеры сцены
WIDTH = 3840
HEIGHT = 2160

# Имя выходного файлы
RENDERED_IMG = "output_image.png"

# Задаем положение камере
CAMERA = Vector(0, -0.35, -1)

# Создаем список объектов 20
OBJECTS = [

    # Создается очень большая сфера для плоскости (Центр, радиус, материал)
    Sphere(
        Point(0, 10000.5, 1),
        10000.0,
        ChequeredMaterial(
            color1=Color.from_hex("#212121"),
            color2=Color.from_hex("#dea971"),
            ambient=0.2,
            reflection=0.2,
        ),
    ),
    # Синяя сфера
    #Sphere(Point(0.75, - 0.1, 1), 0.6, Material(Color.from_hex("#0000FF"))),
    # Розовая сфера
    #Sphere(Point(-0.75, - 0.1, 2.25), 0.6, Material(Color.from_hex("#803980"))),

    Sphere(Point(0.75, - 0.1, 1.5), 0.6, Material(Color.from_hex("#999999"), 0.05, 1, 0.2, 0.5)),
    Sphere(Point(0.4, - 0.1, 4), 0.6, Material(Color.from_hex("#FF97BB"), 0.05, 1, 0.05, 1)),
    Sphere(Point(1.6, 0.4, 1), 0.1, Material(Color.from_hex("#7851A9"), 0.05, 0.7, 0.5, 0.1)),
    Sphere(Point(0.85, 0.4, 0.4), 0.1, Material(Color.from_hex("#1E5945"), 0.05, 0.7, 0.5, 0.5)),
    Sphere(Point(0.6, 0.4, 0.8), 0.1, Material(Color.from_hex("#9932CC"), 0.05, 0.7, 0.5, 0.5)),
    Sphere(Point(0.1, 0.4, 0.25), 0.1, Material(Color.from_hex("#A7FC00"), 0.05, 0.7, 0.5, 0.1)),
    Sphere(Point(-0.1, 0.4, 1.2), 0.1, Material(Color.from_hex("#77DD77"), 0.05, 0.7, 0.5, 0.5)),
    Sphere(Point(-0.37, 0.4, 0.85), 0.1, Material(Color.from_hex("#FFB02E"), 0.05, 0.7, 0.5, 0.5)),
    Sphere(Point(-0.6, 0.4, 1.5), 0.1, Material(Color.from_hex("#ED760E"), 0.05, 0.7, 0.5, 0.5)),
    Sphere(Point(-1, 0.4, 2), 0.1, Material(Color.from_hex("#FF7F50"), 0.05, 0.7, 0.5, 0.1)),
    Sphere(Point(-1.2, 0.4, 1.1), 0.1, Material(Color.from_hex("#FFBD88"), 0.05, 0.7, 0.5, 0.1)),
    Sphere(Point(1.25, 0.4, 0.5), 0.1, Material(Color.from_hex("#B00000"), 0.05, 0.7, 0.5, 0.5)),
    Sphere(Point(1.7, 0.4, 1.7), 0.1, Material(Color.from_hex("#5E2129"), 0.05, 0.7, 0.5, 0.5)),
    Sphere(Point(0.9, 0.4, 0.9), 0.1, Material(Color.from_hex("#C41E3A"), 0.05, 0.7, 0.5, 0.1)),
    Sphere(Point(0.3, 0.4, 0.6), 0.1, Material(Color.from_hex("#293133"), 0.05, 0.7, 0.5, 0.5)),
    Sphere(Point(0, 0.4, 0.7), 0.1, Material(Color.from_hex("#A5A5A5"), 0.05, 0.7, 0.5, 0.5)),
    Sphere(Point(-0.4, 0.4, 0.3), 0.1, Material(Color.from_hex("#6A5ACD"), 0.05, 0.7, 0.5, 1)),
    Sphere(Point(-0.7, 0.4, 0.7), 0.1, Material(Color.from_hex("#77DDE7"), 0.05, 0.7, 0.5, 0.1)),
    Sphere(Point(-1, 0.4, 0.6), 0.1, Material(Color.from_hex("#6495ED"), 0.05, 0.7, 0.5, 0.5)),
    Sphere(Point(-0.2, 0.4, 2.2), 0.1, Material(Color.from_hex("#FF47CA"), 0.05, 0.7, 0.5, 0.5)),
]

# источники света (Центр, цвет)
LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
    Light(Point(-4.5, -10.5, 0), Color.from_hex("#E6E6E6")),
]