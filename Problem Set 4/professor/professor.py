import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        score += check_answer(x, y)

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        num = random.randint(0,9)
    elif level == 2:
        num = random.randint(10,99)
    else :
        num = random.randint(100,999)
    return num

def check_answer(x, y):
    cnt = 0
    while cnt < 3:
        try:
            cnt += 1
            z = int(input(f"{x} + {y} = "))
            if z == x + y:
                return 1
            else:
                print("EEE")
        except ValueError:
            continue

    print(f"{x} + {y} = {x + y}")
    return 0


if __name__ == "__main__":
    main()
