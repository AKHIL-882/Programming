res = [int(n) for n in input().split()]
n = int(input())
for i in res:
    for j in res:
        s = i+j
        if(s%n==0):
            if(i<j):
                print(i,j)
                break
            