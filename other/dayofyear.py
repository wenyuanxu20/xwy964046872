date = "2022-04-29"

year,month,day = (int(x) for x in date.split('-'))

print(day,month,year)

amount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    amount[1] += 1

print(amount)

days = sum(amount[:month-1]) + day

print(days)