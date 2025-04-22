def main():
    spacecraft = {
        "name": "James Webb Space Telescope",
        # "distance": 163,
    }
    spacecraft["distance"] = 163
    spacecraft.update(
        {
            "distance": 0.01,
            "orbit": "Sun",
        }
    )
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft["name"]}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ==========================
    """


main()
