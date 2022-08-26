# factorical of a number
def digit(n):
    if n < 10:
        return 1
    else:
        return 1 + digit(n/10)
n = int(input())
print(digit(n))
