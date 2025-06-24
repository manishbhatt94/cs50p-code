from PIL import Image, ImageFilter


def main():
    with Image.open("in.jpeg") as img:
        print_metadata(img)
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")


def print_metadata(img):
    print(img.size)
    print(img.format)


if __name__ == "__main__":
    main()
