names_list = []
try:
    while True:
        name = input("Name: ")
        names_list.append(name)
except EOFError:
    pass
if len(names_list) == 1:
    print("Adieu, adieu, to",names_list[0])
else:
    for i,name in enumerate(names_list):
        if i == 0:
            names = name
        elif i != len(names_list) - 1 :
            names = names  + ', '+ name
        else:
            if len(names_list) > 2:
                names = names + ', and ' + name
            else:
                names = names + ' and ' + name
    print("Adieu, adieu, to",names)

