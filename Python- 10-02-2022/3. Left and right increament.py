a=int(input())
d=int(input())
n=int(input())
b=a
if(d<0):
    print(a,end=" ")
    for i in range(n-1):
        b = a-(-d)
        print(b, end=" ")
        a=b

else:
    print(a,end=" ")
    for i in range(n-1):
        b = a+d
        print(b, end=" ")
        a=b