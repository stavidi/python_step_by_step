class Timer(object):
    MINUTES = 60
    HOURS = 24
    DAY = MINUTES * HOURS
    def __init__(self, h=0, m=0):
        self.h = h
        self.m = m
        
    def __str__(self):
        return "%02d:%02d" % (self.h, self.m)
        
    def time2min(self):
        return self.h * Timer.MINUTES + self.m
        
    @staticmethod
    def min2time(mm):
        return (mm//Timer.MINUTES) % Timer.HOURS, mm % Timer.MINUTES
        
    def __add__(self, other):
        m1 = self.time2min()
        m2 = other.time2min()
        h, m = self.min2time(m1 + m2)
        return Timer(h, m)
        
    def __sub__(self, other):
        m1 = self.time2min()
        m2 = other.time2min()
        if m1 < m2:
            m1 += Timer.DAY
        h, m = self.min2time(m1 - m2)
        return Timer(h, m)

t1 = Timer(0, 15)
t2 = Timer(1, 10)
print('t1 =', t1)       # t1 = 00:15
print('t2 =', t2)       # t2 = 01:10
print('t1+t2 =', t1+t2) # t1+t2 = 01:25
print('t1-t2 =', t1-t2) # t1-t2 = 23:05
print('t2-t1 =', t2-t1) # t2-t1 = 00:55
