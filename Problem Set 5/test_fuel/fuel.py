def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            continue
        grade = gauge(percentage)
        print(grade)
        break


def convert(fraction):
    nums_list = fraction.split("/")
    try:
        x = int(nums_list[0])
        y = int(nums_list[1])
    except ValueError:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    z = ( x / y ) * 100

    return int(round(z))


def gauge(percentage):
    if not (0 <= percentage <= 100):
        raise ValueError
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
