n = int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count==4):
    print('AES Number')
else:
    print('Not AES Number')
 