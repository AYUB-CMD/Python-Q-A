# 5: state a problem that may be solved with a recursive function and implement
# it is a function which call it self 
# it can use directly mathematical formula as function
# fac(n)=n*fac(n-1)

def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(4) )       