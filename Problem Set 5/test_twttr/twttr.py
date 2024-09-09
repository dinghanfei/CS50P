def main():
    word = input()
    shorten_word = shorten(word)
    print(shorten_word)


def shorten(word):
    str = word
    list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in list:
        str = str.replace(char, "")
    return str

if __name__ == "__main__":
    main()
