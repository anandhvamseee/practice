import calendar
s=list(map(int,input().split()))
day=list(calendar.day_name)
#month=list(calendar.month_name)
dayNumber = calendar.weekday(s[2], s[0], s[1])
o=(day[dayNumber])
print(o.upper())