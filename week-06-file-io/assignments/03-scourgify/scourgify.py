import csv
import sys


def main():
    paths = get_paths_from_cmdargs()
    reformat_data(*paths)


def get_paths_from_cmdargs():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    src, dest = sys.argv[1:]

    if not src.endswith(".csv"):
        sys.exit(f"{src} is not a CSV file")

    if not dest.endswith(".csv"):
        sys.exit(f"{dest} is not a CSV file")

    return src, dest


def reformat_data(src_path, dest_path):
    try:
        with (
            open(src_path, "r", newline="") as src_file,
            open(dest_path, "w", newline="") as dest_file,
        ):
            reader = csv.DictReader(src_file)
            writer = csv.DictWriter(dest_file, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {src_path}")


if __name__ == "__main__":
    main()
