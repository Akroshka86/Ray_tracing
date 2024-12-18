import argparse
import importlib
import os

from scene import Scene
from engine import RenderEngine

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to scene file (without .py extension)")
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)

    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    output_file = mod.RENDERED_IMG.replace(".ppm", ".png")  # Меняем расширение
    image.write_png(output_file)  # Вызываем метод write_png
    print(f"Image saved to {output_file}")

if __name__ == "__main__":
    main()