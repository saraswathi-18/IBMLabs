def do_lcm(a,b):
    if a>b:
        great=a
    else:
        great=b
    while (1):
        if(great%a==0) and (great%b==0):
            lcm=great
            break
        great += 1
    return lcm
a=int(input("enter the number"))
b=int(input("enter the number"))
print("the lcm",do_lcm(a,b))