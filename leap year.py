def is_leap(year):

    leap = False
    # if (year%4 == 0 && year%100 != 0) || (year%400 == 0)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    # write your logic here
    # 3 conditions for a leap year

    # 365.242190 days
    # 23.262222 hours
    # must be divisible by both 100 and 400

    return leap

year = int(input("Enter the year: "))
print(is_leap(year))
