class WeekDayError(Exception):
    pass


class Weeker:
    days =['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day=0):
        self.__days = Weeker.days
        self.__day = day

        if self.__day not in self.__days:
            raise WeekDayError
        self.__day_number = self.__days.index(self.__day )



    def __str__(self):
        return self.__days[self.__day_number]



    def add_days(self, n):
        self.__day_number = (self.__day_number + n) % len(self.__days)



    def subtract_days(self, n):
        self.__day_number = abs((self.__day_number - n) % len(self.__days))






try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
