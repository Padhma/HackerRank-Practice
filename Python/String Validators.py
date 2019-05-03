

if __name__ == '__main__':
    s = str(input())
    for func in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(func(c) for c in s))
        
