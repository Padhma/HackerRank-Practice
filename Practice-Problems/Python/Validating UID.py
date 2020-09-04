import re
for _ in range(int(input())):
    userID = input()
    # (?!.*(.).*\1) -> to check any duplicates
    # (?=(?:.*[A-Z]){2,}) -> to check at least two uppercase letters
    # (?=(?:.*\d){3,}) -> to check at least three numbers
    # [a-zA-Z0-9]{10} -> to check ten alphanumeric characters
    regex = r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$'
    if re.match(regex,userID):
        print('Valid')
    else:
        print('Invalid')

