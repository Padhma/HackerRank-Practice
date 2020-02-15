
for _ in range(int(input())):
    a, b = input().split()

    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e1:
        print("Error Code:",e1)
    except ValueError as e2:
        print("Error Code:",e2)