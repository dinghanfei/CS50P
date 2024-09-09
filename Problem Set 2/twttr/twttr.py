str = input("Input: ")
list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for char in list:
    str = str.replace(char, "")
print("Output:",str)

