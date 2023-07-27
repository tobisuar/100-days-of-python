def is_leap(year):
    if year %4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
                


def days_in_month(year,month):
    if month > 12 or month < 1:
        return "invalid month"
    month_days = [31,28,31,30,31,30,31,30,30,29,30,31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
        
    
year = int(input("ingrese el año"))
month = int(input("ingrese el mes"))
days = days_in_month(year,month)
print(days)