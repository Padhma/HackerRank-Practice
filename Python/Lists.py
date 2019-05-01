if __name__ == '__main__':
    N = int(input())
    arr = []
    for j in range(N):
        i = input().split(" ")
        command = i[0]
        if command == 'insert':
            arr.insert(int(i[1]),int(i[2]))
        elif command == 'print':
            print(arr)
        elif command == 'remove':
            arr.remove(int(i[1]))
        elif command == 'append':
            arr.append(int(i[1]))
        elif command == 'sort':
            arr.sort()
        elif command == 'pop':
            arr.pop()
        elif command == 'reverse':
            arr.reverse()
