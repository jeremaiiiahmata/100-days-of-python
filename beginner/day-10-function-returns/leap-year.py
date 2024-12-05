def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Enter what year: "))

isLeap = is_leap_year(year)

if isLeap == True:
    print(f"{year} is a leap year!")
else :
    print(f"{year} is not a leap year!")