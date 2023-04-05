import calendar
print(calendar.calendar(2023, m=3))
#calendar.prcal(2020, m=1)


c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")

c = calendar.Calendar()

for iter in c.itermonthdays3(2019, 11):
    print(iter, end=" ")

for iter in c.itermonthdays4(2019, 11):
    print(iter, end=" ")

for data in c.monthdays2calendar(2020, 12):
    print(data)