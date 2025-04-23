SHOWS = [
    " avatar: The last airbender",
    "Ben 10",
    "Arthur",
    "  spongebob Squarepants",
    "Phineas and ferb",
    " kim possible",
    "Jimmy neutron ",
    "the Proud family ",
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print("\n".join(cleaned_shows))


main()
