class clockTime:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    def setHours(self, hours):
        self.hours = hours
    def setMinutes(self, minutes):
        self.minutes = minutes
    def setSeconds(self, seconds):
        self.seconds = seconds
    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def showTime(self):
        time = "{}:{}:{}".format(self.hours, self.minutes, self.seconds)
        return time

newTime = clockTime()
hrs = int(input("Enter the hours' value: "))
newTime.setHours(hrs)
mins = int(input("Enter the minutes' value: "))
newTime.setMinutes(mins)
s = int(input("Enter seconds' value: "))
newTime.setSeconds(s)
print ("The time is: ", newTime.showTime())