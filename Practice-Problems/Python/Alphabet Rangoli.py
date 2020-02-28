import string
character = string.ascii_lowercase

def print_rangoli(n):
    Rangoli = []

    for i in range(n):
        s = '-'.join(character[i:n])
        Rangoli.append(s[::-1]+s[1:])

    w = len(Rangoli[0])

    for i in range(n-1,0,-1):
        print(Rangoli[i].center(w, '-'))

    for i in range(n):
        print(Rangoli[i].center(w, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)