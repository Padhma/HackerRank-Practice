from collections import namedtuple

n, columns = int(input()), input()
student = namedtuple('student', columns)
marksSum = 0
for _ in range(n):
    Student = student(*input().split())
    marksSum += int(Student.MARKS)
print("{:.2f}".format(marksSum/n))

