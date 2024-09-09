from validator_collection import validators, errors

email = input("What's your email adress? ").strip()
try:
    validated_email = validators.email(email)
    print("Valid")
except errors.EmptyValueError:
    print("Empty email")
except errors.InvalidEmailError:
    print("Invalid")

