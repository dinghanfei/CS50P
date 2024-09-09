sum_money = 0
while sum_money < 50:
    print(f"Amount Due: {50 - sum_money}")
    money = int(input("Insert Coin: "))
    if money == 25 or money == 10 or money == 5:
        sum_money += money

print("Change Owed:" ,sum_money - 50)


