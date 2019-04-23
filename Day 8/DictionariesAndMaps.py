# Enter your code here. Read input from STDIN. Print output to STDOUT

phoneBook = {}

n = int(input())

phoneBook = dict(input().split() for _ in range(n))

# print(phoneBook)

while True:
    name = input()
    if name in phoneBook:
        #print(name + "=" + phoneBook[name])
        print("{}={}".format(name,phoneBook[name]))
    else:
        print("Not found")
    
    if name == "":
        break
