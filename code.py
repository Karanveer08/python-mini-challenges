# --------------
#Code starts here
def palindrome(num):
    for i in range(num+1,2*num):
        if str(i)==str(i)[::-1]:
            return i
palindrome(123)
palindrome(1331)



# --------------
#Code starts here
def a_scramble(str_1, str_2):
    str_1 = list(str_1.lower())
    str_2 = list(str_2.lower())
    for i in range(0, len(str_2)):
        if str_2[i] in str_1:
            str_1.remove(str_2[i])
            if i == len(str_2) - 1:
                return True
        else: 
            return False
a_scramble("Tom Marvolo Riddle","Voldemort")
a_scramble("ticket","chat")


# --------------
#Code starts here
from math import sqrt
 
def is_perfect_square(x):
 
    s = sqrt(x)
    return (int(s)*int(s) == x) 
 

def check_fib(num):
    if is_perfect_square((5*num*num) + 4) or is_perfect_square((5*num*num) - 4): #Formula f
        return True
    
    return False     


# --------------
def compress(word):
    word=word.lower()
    result = ""
    count = 1
    #Add in first character
    result += word[0]
    #Iterate through loop, skipping last one
    for i in range(len(word)-1):
        if(word[i] == word[i+1]):
            count+=1
        else:
            result += str(count)
            result += word[i+1]
            count = 1
    result += str(count)        
    return result


# --------------
#Code starts here
def k_distinct(string,k):
    string = string.lower()
    unique = []
    for char in string[::]:
        if char not in unique:
            unique.append(char)
    count = len(unique)
    
    if count==k:
        return True
    else:
        return False
    


