ans = input("What is the Answer to the Great Question of Life, the Universe, and Everthing? ")
ans = ans.lower()
ans = ans.strip()
if ans == "42" or ans == "forty-two" or ans == "forty two":
    print("Yes")
else:
    print("No")
