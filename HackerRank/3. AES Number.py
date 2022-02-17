val = int(input())
count=0
for i in range(1,val+1):
    if((val%i)==0):
        count=count+1
if(count==4):
    print("AES number")
else:
    print("Not a AES number")