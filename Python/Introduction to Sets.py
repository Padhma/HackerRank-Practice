def average(array):
    newSet = set(array)
    lengthOfSet = len(newSet)
    sumOfSet = sum(newSet)
    return sumOfSet/lengthOfSet

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)