# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()

for i in range(int(n)):
    s = list(input())
    evenIndex = list()
    oddIndex = list()
    letter = 0
    for char in s:
        if letter % 2 == 0:
            evenIndex.append(char)
        else:
            oddIndex.append(char)
        letter += 1
    evenString = "".join(evenIndex)
    oddString = "".join(oddIndex)
    print("%s %s" % (evenString, oddString))
            

    
