a=int(input("enter the number"))
if a>1:
    for i in range(2,a):
        if(a%i==0):
            print("{} is not prime number".format(a))
            break
    else:
        print("{} is prime number".format(a))
else:
    print("{} is not prime".format(a))
