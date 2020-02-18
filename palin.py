name = input("enter the name")
name = name.casefold()
rev = reversed(name)
if list(name) == list(rev):
    print("the name is palindrome")
else:
    print("not a palindrome")
