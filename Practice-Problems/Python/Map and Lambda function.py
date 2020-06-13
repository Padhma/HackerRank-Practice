cube = lambda x: x**3

def fibonacci(n):
    fib_list = []
    first, second = 0, 1
    for i in range(n):
        if i <= 1:
            next_ele = i
        else:
            next_ele = first + second
            first, second = second, next_ele
        fib_list.append(next_ele)
    return fib_list
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))