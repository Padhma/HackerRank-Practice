import statistics

n = int(input())
numArray = [int(n) for n in input().split()]

print(round(statistics.pstdev(numArray),1))
