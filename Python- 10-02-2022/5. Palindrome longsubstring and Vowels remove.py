# def longestPalSubstr(string):
# 	n = len(string)
# 	if (n < 2):
# 		return n
# 	start=0
# 	maxLength = 1
# 	for i in range(n):
# 		low = i - 1
# 		high = i + 1
# 		while (high < n and string[high] == string[i] ):							
# 			high=high+1
	
# 		while (low >= 0 and string[low] == string[i] ):				
# 			low=low-1
	
# 		while (low >= 0 and high < n and string[low] == string[high] ):
#     		low=low-1
# 		    high=high+1
		
	
# 		length = high - low - 1
# 		if (maxLength < length):
# 			maxLength = length
# 			start=low+1
# 	print (string[start:start + maxLength])
	
# 	return maxLength
# val = int(input())
# userlist = []
# for i in range(0,val):
#     string = int(input())
#     userlist.append(string)
# for i in range(len(userlist)):
#     print(longestPalSubstr(i))

# import re
# def rem_vowel(string):
#     return (re.sub("[aeiouAEIOU]","",string))           

# def is_vow(c):
# 	return ((c == 'a') or (c == 'e') or
# 			(c == 'i') or (c == 'o') or
# 			(c == 'u'));
# def removeVowels(str):
# 	print(str[0], end = "");
# 	for i in range(1,len(str)):
# 		if ((is_vow(str[i - 1]) == True) or (is_vow(str[i]) == True)):
# 		    print(str[i], end = "")
# 		else:
# 		    vowels = ['a','e','i','o','u']
# 		    result = [letter for letter in str if letter.lower() not in vowels]
# 		    result = ''.join(result)
# 		    print(result)

# # Driver code
# str= input()
# removeVowels(str)


# Python program to remove vowels from a string
# Function to remove vowels
def is_vow(c):
	return ((c == 'a') or (c == 'e') or
			(c == 'i') or (c == 'o') or
			(c == 'u'));
def rem_vowel(string):
	vowels = ['a','e','i','o','u']
	result = [letter for letter in string if letter.lower() not in vowels]
	result = ''.join(result)
	print(string[0], end = "")
	for i in range(1,len(string)):
		if ((is_vow(string[i - 1]) == True) or (is_vow(string[i]) == True)):
		    print(string[i], end = "")
	#print(result)
# Driver program
string = input()
rem_vowel(string)










