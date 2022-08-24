import numpy as np
l = []
loop = int(input())
for i in range(0,loop):
    n = int(input())
    arr = []
    arr = [int(n) for n in input().split()]
    res = np.unique(arr)
    if(len(arr)==len(res)):
        l.append(len(arr))
    else:
        l.append(len(res))
for i in l:
    print(i)
    
