from calendar import Calendar

class MyCalendar(Calendar):
    def __init__(self):
        Calendar.__init__(self)

    def count_weekday_in_year(self, year, weekday):
        self.year = year
        self.weekday = weekday
        wd_count = 0
        #c = Calendar()
        for self.month in range(1,13):
            for data in Calendar.monthdays2calendar(self, self.year, self.month):
                for i in data:
                    if i[0] !=0 and i[1] == self.weekday: wd_count +=1
                # print(data)
        print("Weekday ",self.weekday, " count in year ", self.year, " is ", wd_count)

weekdaysofyear = MyCalendar()
weekdaysofyear.count_weekday_in_year(20,0)


#print(dir(MyCalendar))