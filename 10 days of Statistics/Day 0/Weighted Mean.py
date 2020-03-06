# Enter your code here. Read input from STDIN. Print output to STDOUT

n = map(int,input().split())

values = list(map(int, input().strip().split(' ')))
weights = list(map(int, input().strip().split(' ')))

s = 0
for x,y in zip(values, weights):
    s += x*y

weightedMean = s / sum(weights)
print(round(weightedMean,1))
