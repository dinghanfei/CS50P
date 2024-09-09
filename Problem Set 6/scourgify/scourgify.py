import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as before_file, open(sys.argv[2], "w", newline="") as after_file:
            reader = csv.DictReader(before_file)
            writer = csv.DictWriter(after_file, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                lastname, firstname = row["name"].strip().split(", ")
                writer.writerow(
                    {
                        "first" : firstname,
                        "last" : lastname,
                        "house" : row["house"]
                    }
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")





