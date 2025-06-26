import os
import sys

from PIL import Image, ImageOps

SHIRT_IMAGE_PATH = "shirt.png"


def main():
    paths = get_paths_from_cmdargs()
    overlay_cs50_shirt(*paths)


def get_paths_from_cmdargs():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    src, dest = sys.argv[1:]

    src_ext = os.path.splitext(src.lower())[1]
    dest_ext = os.path.splitext(dest.lower())[1]

    if src_ext not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")

    if dest_ext not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")

    if src_ext != dest_ext:
        sys.exit("Input and output have different extensions")

    return src, dest


def overlay_cs50_shirt(input_path, output_path):
    try:
        with Image.open(input_path) as img, Image.open(SHIRT_IMAGE_PATH) as shirtImg:
            img = ImageOps.fit(image=img, size=shirtImg.size)
            img.paste(im=shirtImg, mask=shirtImg)
            img.save(output_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
