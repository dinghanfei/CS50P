while True:
    nums = input("Fraction: ")
    nums_list = nums.split("/")
    try:
        x = int(nums_list[0])
        y = int(nums_list[1])
    except ValueError:
        continue
    if x > y:
        continue
    try:
        z = ( x / y ) * 100
    except ZeroDivisionError:
        continue
    else:
        break

z = int(round(z))
if z <= 1:
    print("E")
elif z >= 99:
    print("F")
else:
    print(f"{z}%")



