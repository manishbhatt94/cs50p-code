from artists import get_artists
from artwork import get_artworks


def main():
    find_artists()


def find_artworks():
    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")


def find_artists():
    artist = input("Artist: ")
    artists = get_artists(query=artist, limit=3)
    for artist in artists:
        print(f"* {artist}")


main()
