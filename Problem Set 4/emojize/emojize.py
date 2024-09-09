from emoji import emojize
str = input("Input: ").strip()
emoji = emojize(str, language='alias')
print("Output:",emoji)
