#huddle race
array_size = int(input())
height_person = int(input())
height_array = [int(n) for n in input().split()]
res = max(height_array) - height_person)
if(res):
    print(res)
else:
    print(0)
