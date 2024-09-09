import re


def main():
    print(count(input("Text: ")))


def count(s):
    substring = r"\bum\b"
    matches = re.findall(substring, s, flags=re.IGNORECASE)
    num = len(matches)
    return num


if __name__ == "__main__":
    main()
