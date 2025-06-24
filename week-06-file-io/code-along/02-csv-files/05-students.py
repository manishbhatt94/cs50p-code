import csv

# Writing a row of data each time this program is run to an
# initially blank CSV file that just has the header row

name = input("What's your name? ")  # Harry
home = input("Where's your home? ")  # Number Four, Privet Drive

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
