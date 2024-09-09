def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def has_punctuation(str):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for char in str:
        if char in punctuation:
            return True
    return False


def has_valid_digit(str):
    first_index = -1
    for i,char in enumerate(str):
        if char.isdigit():
            first_index = i
            break
    # 不含数字
    if first_index == -1:
        return True
    if not str[first_index:].isdigit():
        return False
    if str[first_index] == '0':
        return False
    return True


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return  False
    if not has_valid_digit(s):
        return False
    if s.count(".") != 0 or s.count(" ") != 0 or has_punctuation(s):
        return False
    return True


main()
