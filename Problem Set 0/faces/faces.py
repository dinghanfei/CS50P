def convert(str):
    str = str.replace(':)','🙂')
    str = str.replace(':(','🙁')
    print(str)

def main():
    str = input()
    str = convert(str)


main()

