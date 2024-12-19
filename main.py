import argparse
import importlib
import os

from scene import Scene
from engine import RenderEngine

# python main.py examples.twoballs
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to scene file (without .py extension)")
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)

    # Создание объекта сцены для рендеринга
    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine()

    # Рендеринг изображения
    image = engine.render(scene)

    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    output_file = mod.RENDERED_IMG.replace(".ppm", ".png")

    # Сохранение изображения в png
    image.write_png(output_file)
    print(f"Image saved to {output_file}")

if __name__ == "__main__":
    main()