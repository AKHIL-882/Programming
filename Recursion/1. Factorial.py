# factorical of a number
def fact(n):
    if(n<1):
        return 1
    else:
        s = n * fact(n-1)
    return s
n = int(input())
print(fact(n))

