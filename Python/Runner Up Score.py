if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    maximum = max(arr)

    while max(arr) == maximum:
        arr.remove(max(arr))

    print(max(arr))

