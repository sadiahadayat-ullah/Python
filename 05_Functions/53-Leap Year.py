def leap_year(year):
    if year % 400 == 0:
        return "Leap Year"
    elif year % 100 == 0:
        return "Not Leap Year"
    elif year % 4 == 0:
        return "Leap Year"
    else:
        return "Not Leap Year"
print(leap_year(2000))