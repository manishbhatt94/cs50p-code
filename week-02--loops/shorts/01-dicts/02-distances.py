distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "Pioneer 11": 44,
    "New Horizons": 58,
    "James Webb Space Telescope": 0.01,
}


def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")

    print()

    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")


def convert(au):
    """Converts Astronomical Units (AU) to Metres (m)"""
    return au * 149597870700


main()
