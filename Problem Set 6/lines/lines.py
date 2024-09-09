import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        try:
            LOC = 0
            with open(sys.argv[1]) as file:
                for line in file:
                    line = line.lstrip()
                    if len(line) == 0 or line.startswith("#"):
                        continue
                    else:
                        LOC += 1
        except FileNotFoundError:
            sys.exit("File does not exist")
print(f"{sys.argv[1]} has {LOC} lines of code")


