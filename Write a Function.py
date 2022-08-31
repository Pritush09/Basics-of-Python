def is_leap(year):
    leap = False
    if year%4==0:#jab tak 100 se devide hoke 0 naade
        leap = True
        if year%100 == 0:
            leap = False
            if year%400==0:
                leap = True
    return leap

year = int(input())
print(is_leap(year))