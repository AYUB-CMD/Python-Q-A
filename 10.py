# prime number
num=int(input("enter your number : "))

if num > 1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not prime")
            break
        else:
            print(num,"its a prime")
            break 
else:
            print(num,"its a prime")                