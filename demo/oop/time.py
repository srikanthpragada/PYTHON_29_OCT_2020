class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    @property
    def hours(self):
        return self.h

    @hours.setter
    def hours(self, value):
        if value >= 0 and value <= 23:
            self.h = value
        else:
            raise ValueError("Invalid Hour")

    @property
    def totalseconds(self):
        return self.h * 3600 + self.m * 60 + self.s


t = Time(10, 20, 30)
t.hours = 5     # call setter method of hours property
print(t.hours)  # call getter method of hours property
print(t.totalseconds)
