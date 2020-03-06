from statistics import median

n = int(input())
numArray = [int(n) for n in input().split()]
numArray.sort()
mid = int(n // 2)

if n % 2 == 0:
    lower = numArray[:mid]
    upper = numArray[mid:]
else:
    lower = numArray[:mid]
    upper = numArray[mid+1:]

print(int(median(lower)))
print(int(median(numArray)))
print(int(median(upper)))
