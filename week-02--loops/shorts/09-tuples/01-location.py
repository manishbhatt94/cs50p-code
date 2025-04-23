import sys


def main():
    coordinates = (42.376, -71.115)
    print(f"Latitide: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")

    # unpacking a tuple
    latitude, longitude = coordinates
    print(f"Latitide: {latitude}")
    print(f"Longitude: {longitude}")

    # tuples are immutable (they can't be reassigned to)
    # TypeError: 'tuple' object does not support item assignment
    # coordinates[0] = -1 * coordinates[0]

    # Memory comparison of tuples vs lists
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = (42.376, -71.115)
    print(f"Tuple size = {sys.getsizeof(coordinate_tuple)} bytes")
    print(f"List size = {sys.getsizeof(coordinate_list)} bytes")


main()
