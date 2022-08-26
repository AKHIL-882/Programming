# factorical of a number
def natural(n):
    if(n==0):
        return 1
    else:
        natural(n-1)
        print(n)

n = int(input())
natural(n)

