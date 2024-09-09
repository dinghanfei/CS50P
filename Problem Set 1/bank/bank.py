greet = input("Greeting: ").lstrip()
greet = greet.lower()
if greet.startswith("hello") :
    print("$0")
elif greet.startswith('h') :
    print("$20")
else :
    print("$100")
