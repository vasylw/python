from datetime import date, time

d = date(1991, 2, 5)
print(d)

d = d.replace(1, 12, 18)
print(d)


from datetime import date

d = date(2019, 11, 4)
print(d.weekday())



t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
