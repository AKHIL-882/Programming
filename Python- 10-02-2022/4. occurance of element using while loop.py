# defining the function
def NO(x,a):
    count=0
    i=0
    # while loop to iterate
    while(i!=len(a)):
        if(x==a[i]):
            count=count+1
        i=i+1
    #returing the frequencies
    return count
        
# getting the size of list
n = int(input())
# getting the list of elements
a = [int(n) for n in input().split()]
# getting the element to find the occurrances
x = int(input())
# displaying the result
print(NO(x,a))
    
    