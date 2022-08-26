def jos(n,k):
    if(n==1):
        return 0
    else:
        return (jos(n-1,k)+k)%n
        
n = int(input())
k = int(input())
print(jos(n,k))
