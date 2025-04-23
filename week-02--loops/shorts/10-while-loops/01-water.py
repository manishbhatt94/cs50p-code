from soil import sample


def main():
    days = 0
    moisture = sample()
    print(f"Day {days}: Moisture is {moisture}%")

    while moisture > 20:
        days += 1
        moisture = sample()
        print(f"Day {days}: Moisture is {moisture}%")

    print("Time to water!")


main()
