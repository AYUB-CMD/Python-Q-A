# factorial
n=int(input('enter your fac number : '))
def factorial(n):
    fac =1
    if n <0:
        print("sorry, factorial does not exist for nagative numbers")
    elif n == 0:
        print("factorial for number 0 is 1")
    else:
        for i in range(1,n+1):
            fac=fac*i  
        print("factorial of",n,"is",fac)   


factorial(n)