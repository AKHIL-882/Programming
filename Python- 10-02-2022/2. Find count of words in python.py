# importing libraries
import re
# declaring the function
def wordCount(str):
    # spliting the string
    str = str.split()         
    str2 = []
    # checking the conditions
    for i in str:             
        if i not in str2:
            str2.append(i) 
    for i in range(0, len(str2)):
        # displaying the result
        print(str2[i], ' - ', str.count(str2[i]))    

# getting the string from the user
str = input()
# removing punctuations
str = re.sub(r'[^\w\s]',"",str)
# calling the function
wordCount(str)                    
  
