# fibonacci
nthTerms = int(input("How many terms ? : "))

n1,n2=0,1
count=0

if nthTerms <=0:
    print("enter positive number")
elif nthTerms ==1:
    print(f"fibonacci sequnece upto {nthTerms} :")
    print(n1)
else:
    print("fibonacci sequence") 
    while count < nthTerms:
        print(n1)
        nth=n1+n2 
        #update values
        n1=n2
        n2=nth
        count = count+1
        


