from random import randint
while True:
    try:
        num = int(input("Level: "))
    except ValueError:
        continue
    if num < 1:
        continue
    else:
        ans = randint(1, num)
        break
while True:
    try:
        num = int(input("Guess: "))
    except ValueError:
        continue
    if num < 0:
        continue
    if num == ans:
        print("Just right!")
        break
    elif num > ans:
        print("Too large!")
    else:
        print("Too small!")
