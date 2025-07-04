import csv

import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as views, open("analysis-1.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            row["brightness"] = round(brightness, 2)
            writer.writerow(row)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


if __name__ == "__main__":
    main()
