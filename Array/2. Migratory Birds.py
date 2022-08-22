#huddle race
import numpy as np
size = int(input())
freq_array = [0] * size
birds_id =[int (n) for n in input ().split ()]
for i in birds_id:
    for j in birds_id:
        if(i==j):
            freq_array[i]+=1
            break
val = freq_array[0]
for i in range(len(freq_array)):
    if(val<freq_array[i]):
        val = freq_array[i]
print(freq_array.index(val))
    
# print(freq_array)  
# dup = []
# for i in freq_array:
#     if(i not in dup):
#         dup.append(i)
# print(freq_array.index(max(freq_array)))
 


