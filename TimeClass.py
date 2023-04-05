class Timer:

    def __init__(self, hh=0, mm=0, ss=0):
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    def __str__(self):
        hh = str(self.__hh)
        mm = str(self.__mm)
        ss = str(self.__ss)
        if len(hh) == 1: hh = '0' + hh
        if len(mm) == 1: mm = '0' + mm
        if len(ss) == 1: ss = '0' + ss

        time = hh+':'+mm+':'+ss
        return time

    def next_second(self):
        self.__ss +=1
        if self.__ss > 59:
            self.__ss = 0
            self.__mm +=1

        if self.__mm > 59:
            self.__mm = 0
            self.__hh +=1

        if self.__hh > 23:
            self.__hh = 0


    def prev_second(self):
        self.__ss -= 1

        if self.__ss < 0:
            self.__ss = 59
            self.__mm -=1

        if self.__mm < 0:
            self.__mm = 59
            self.__hh -= 1

        if self.__hh < 0:
            self.__hh = 23





timer = Timer(23, 59, 59)
#print(timer.str())
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

#print(timer._Timer__ss)
