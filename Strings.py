
    
#reverse of a string
# str = input()       
# str1 = ""   
# for i in str:  
#     str1 = i + str1 
#     print(str1)
# print(str1) 


# Palindrome number
# st = input()
# reverse_st = st[::-1]
# if(st==reverse_st):
#     print('Palindrome')
# else:
#     print('Not Palindrome')


# counting number of spaces and words
# st = input()
# space_count = 0
# for i in st:
#     if(i==" "):
#         space_count+=1
# print(space_count,space_count+1)


# counting number of character occurred
# st = input()
# char = input()
# print(st.count(char))



# counting number of vowels in a string 
# st = input()
# l = ['a','e','i','o','u']
# count=0
# for i in st:
#     if i in l:
#         count+=1
# print(count)


# removing vowels from a string
# st = input()
# l = ['a','e','i','o','u']
# temp = ''
# for i in st:
#     if i in l:
#         temp+=''
#     else:
#         temp+=i
# print(temp)


#balance Parentisis
# st = input()
# count_right, count_left = 0,0
# for i in st:
#     if(i==')'):
#         count_right+=1
#     if(i=='('):
#         count_left+=1
# if(count_left==count_right):
#     print('Balanced')
# else:
#     print('Not Balanced')


# funny string
# cases = int(input())
# for caseNo in range(cases):
#     s = input()
#     rs = s[::-1]
#     n = len(s)
#     for i in range(1, n):
#         d1 = abs(ord(s[i]) - ord(s[i - 1]))
#         d2 = abs(ord(rs[i]) - ord(rs[i - 1]))
#         if d1 != d2:
#             print("Not Funny")
#             break
#     else:
#         print("Funny")
     
# string password
# password = input()
# num = '1234567890'
# special = '!@#$%^&*()-+'
# count_num,count_lower,count_upper,count_special = 0,0,0,0
# if(len(password)>=6):
#     for i in password:
#         if i in num:
#             count_num+=1
#         if i.islower() == True:
#             count_lower+=1
#         if i.isupper() == True:
#             count_upper+=1
#         if i in special:
#             count_special+=1
            
# if(count_num>1 and count_special>1 and count_upper>1 and count_lower>1):
#     print('Strong Password')
# else:
#     print("Not strong Password")

            
# Mars Exploration

# s = 'SOS'
# st = input()
# count=0
# for i in st:
#     if i in s:
#         pass
#     else:
#         count+=1
# print(count)


# String camel case

# st = input()
# count=0
# for i in st:
#     if i.isupper() == True:
#         count+=1
# print(count)
    
    

    











