k = int(input())
array =[int (n) for n in input ().split()]
odd_array = [i for i in range(k*k) if(i%2)!=0]
temp3 = []
for element in odd_array:
    if element not in array:
        temp3.append(element)
print(temp3[0])

 