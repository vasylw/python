from datetime import datetime

dt = datetime(2020, 11, 4, 14, 53,00)

print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("Week number of the year: %W"))
