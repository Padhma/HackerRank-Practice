import calendar as c

def convertWeekDay(weekDay):
    switcher = {
        0: "MONDAY",
        1: "TUESDAY",
        2: "WEDNESDAY",
        3: "THURSDAY",
        4: "FRIDAY",
        5: "SATURDAY",
        6: "SUNDAY"
    }
    return switcher.get(weekDay, "nothing")


month, day, year = input().split()

weekDay = c.weekday(int(year), int(month), int(day))

print(convertWeekDay(weekDay))