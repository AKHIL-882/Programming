sum_=0
if __name__ == '__main__':
	a, b, i, j, flag = 0, 0, 0, 0, 0
	a = int(input()) 
	b = int(input())
	for i in range(a, b + 1):
		if (i == 1):
			continue
		flag = 1
		
		for j in range(2, abs(i) // 2 + 1):
			if (abs(i) % abs(j) == 0):
				flag = 0
				break
		if (flag == 1):
		    sum_ = sum_ + i
print(sum_)