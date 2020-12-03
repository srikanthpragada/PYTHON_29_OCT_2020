import pickle
import json


class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"


t = Time(10, 20, 30)
f = open("time.pickle", "wb")
pickle.dump(t, f)
f.close()

f = open("time.pickle","rb")
t = pickle.load(f)
print(t)

print(json.dumps(t.__dict__))