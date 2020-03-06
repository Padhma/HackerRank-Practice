from statistics import median

n = int(input())
elementArray = [int(n) for n in input().split()]
frequencyArray = [int(n) for n in input().split()]

datasetArray = []
for i in range(n):
    datasetArray += [elementArray[i]] * frequencyArray[i]

N = len(datasetArray)
datasetArray.sort()
mid = int(N // 2)

if N % 2 == 0:
    lower = datasetArray[:mid]
    upper = datasetArray[mid:]
else:
    lower = datasetArray[:mid]
    upper = datasetArray[mid+1:]

print(round(float(int(median(upper))-int(median(lower))),1))
