num=int(input("enter the number"))
fact = 1
if num < 0:
    print("negative values")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact = fact * i

print("the factorial is", fact)
