val = int(input())
count = 0
l = []
for i in range(0,2*val):
    if(i%2!=0):
        count = count+1
        l.append(i)
        if(count==val):
            break
print(l)
userList = [int(n) for n in input().split()]
for i in l:
    if(i not in userList):
        print(i)
