import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            table = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                headers = next(reader)  # 使用next()函数获取迭代器的第一个元素
                for row in reader:
                    table.append(row)

        except FileNotFoundError:
            sys.exit("File does not exist")
print(tabulate(table, headers = headers, tablefmt="grid"))
