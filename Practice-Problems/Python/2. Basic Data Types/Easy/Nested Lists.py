n = int(input())
markSheet = [[input(),float(input())] for _ in range(n)]

secondMaximum = sorted(list(set([score for name, score in markSheet])))[1]
print('\n'.join([studentName for studentName,marks in sorted(markSheet) if marks == secondMaximum]))
