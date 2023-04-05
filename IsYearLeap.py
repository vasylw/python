
def is_year_leap(year):

    if (year%4 == 0 and year%100 != 0) or  year%400 == 0:
        leap = True
    else:
        leap = False

    return leap

year = int(input("Type a year, for leap checking:"))

if is_year_leap(year) == False:
    print ("Year " + str(year) + " isn't leap")

if is_year_leap(year):
    print ("Year " + str(year) + " is leap")

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")