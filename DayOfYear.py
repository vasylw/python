
def is_year_leap(year):

    if (year%4 == 0 and year%100 != 0) or  year%400 == 0:
        leap = True
    else:
        leap = False

    return leap

# print(str(leap))

ndays_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month(year, month):
    leap = is_year_leap(year)

    if leap:
        if month == 2:
            days = int(ndays_in_month[month-1]+1)
        if month >= 1 and month <= 12 and month !=2:
            days = ndays_in_month[month-1]
        return days
    elif leap == False:
        if month >= 1 and month <= 12:
            days = ndays_in_month[month-1]
        return days
    else:
        return None

def day_of_year(year, month, day):
    d_o_y = 0
    if month <=0 or month > 12 or day > 31:
        return None

    elif is_year_leap(year):
        for m in range(month-1):
            d_o_y = d_o_y + ndays_in_month[m]
        return d_o_y + day + 1
    else:
        for m in range(month-1):
            d_o_y = d_o_y + ndays_in_month[m]
        return d_o_y + day

#
# Write your new code here.
#

print("Day of year:", day_of_year(2000, 4, 1))


# year = int(input("Type a year, for checking:"))
# month = int(input("Type a month number, for days checking:"))

#print ("Days in month " + str(month) + " of year " + str(year)+ " are " + str(days_in_month(year, month)))


#print(str(is_year_leap(year)))

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
