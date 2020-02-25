yr=int(input("enter the year"))
if(yr%4)==0:
    if(yr%100)==0:
        if(yr%400)==0:
            print("{} is leap year".format(yr))
        else:
            print("{} is not leap year".format(yr))
    else:
        print("{} is a leap year".format(yr))
else:
    print("{} is not leap year".format(yr))