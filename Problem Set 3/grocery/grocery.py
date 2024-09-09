shopping_dic = {}
try:
    while True:
        item = input().upper()
        if item in shopping_dic:
            shopping_dic[item] += 1
        else:
            shopping_dic[item] = 1
except EOFError:
    pass

shopping_things = sorted(shopping_dic.keys())

for key in shopping_things:
    val = shopping_dic[key]
    print(f"{val} {key}")

