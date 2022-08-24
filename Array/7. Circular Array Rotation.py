import numpy as np
arr = [int(n) for n in input().split()]
k = int(input())
myarray = np.array(arr)
newarray = np.roll(myarray, k)
queries = [int(n) for n in input().split()]
for i in range(len(newarray)):
    for i in queries:
        print(newarray[i],end=" ")
    break

    