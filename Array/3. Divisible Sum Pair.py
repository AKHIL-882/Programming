k = int(input())
array =[int (n) for n in input ().split()]
for i in array:
    for j in array:
        if(i<j):
            if((i+j)%k==0):
                print(i,j)
        continue


