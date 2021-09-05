# 7:given array of integer decide if it is palindrome

# String pallindrome

# def isPallindrome(s):
#     s=s.lower()
#     l=len(s)

#     if l < 2:
#         return True
#     elif s[0] == s[l-1]:
#         return isPallindrome(s[1:l-1]) 
#     else:
#         return False

# s ='malayalam'
# ans =isPallindrome(s)
# if ans:
#     print('yes')
# else:
#     print('no')    


# array of integer decide if it is palindrome
# def p(s):
#     if s == s[::-1]:
#         print(f"yes it is pallindrome {s} = {s[::-1]}")
#     else:
#         print("no it is not")   

# p('racecar')         

arr=[1,2,2,2,1]
arr1=[2,3,5,56,7]

def pal(arr):
    try:
        for i in arr:
            if arr == arr[::-1]:
                print(f"yes it is pallindrome {arr} = {arr[::-1]}")
                break
            else:
                print(f"no it is not {arr} = {arr[::-1]} ")   
                break
    except Exception(e):
        print(e)
pal(arr) 


       