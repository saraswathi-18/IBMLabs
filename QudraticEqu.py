import cmath
a=1
b=int(input("enter b number"))
c=int(input("enter c number"))
answer=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(answer))/(2*a)
sol2=(-b+cmath.sqrt(answer))/(2*a)
print("the answer is {0} and {1}".format(sol1,sol2))