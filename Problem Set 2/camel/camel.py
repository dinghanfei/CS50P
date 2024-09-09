str = input("camelCase: ")
str_list = []
current_str = ""
for i in range(len(str)):
    if str[i].islower():
        current_str += str[i]
    else:
        if current_str:
            str_list.append(current_str)
        current_str = str[i].lower()

if current_str:
    str_list.append(current_str)

snake_str = "_".join(str_list)
print("snake_case:", snake_str)
