import math

class Direction(object):
    def __init__(self, dx=0, dy=0):
        self.dx = dx
        self.dy = dy
        
    def __str__(self):
        return '{} {}'.format(self.dx, self.dy)

    def __repr__(self):
        return 'Direction({}, {})'.format(self.dx, self.dy)

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '{} {}'.format(self.x, self.y)
        
    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)
        
    def move(self, dir=None):
        if dir is None:
            return
        self.x += dir.dx
        self.y += dir.dy
        
    def dir(self, other=None):
        if other is None:
            other = Point(0, 0)
        dx = self.x - other.x
        dy = self.y - other.y
        return Direction(dx, dy)
        
    def dist2(self, other):
        """Квадрат расстояния до точки other"""
        dx = self.x - other.x
        dy = self.y - other.y
        return dx*dx + dy*dy
       
    def dist0(self):
        """Квадрат расстояния до точки (0,0)"""
        return dist2(Point(0,0))
        
class Segment2(object):
    def __init__(self, start=None, finish=None):
        self.start = start or Point()
        self.finish = finish or Point()
        
    def __str__(self):
        return '{} {}'.format(self.start, self.finish)
        
    def __repr__(self):
        return '({}, {})'.format(repr(self.start), repr(self.finish))
    
    def length2(self):
        return self.start.dist2(self.finish)
        
    def length(self):
        return math.sqrt(self.length2())
        
    def move(self, dir=None):
        self.start.move(dir)
        self.finish.move(dir)
    
    def left(self):
        return self.start.x
        
'''Дан список отрезков по 1 отрезку на строку в формате x1 y1 x2 y2 (целые числа через пробел). 
Напечатать эти отрезки, выровненные по левому краю.'''

import sys

a = []
for str in sys.stdin:
    x1, y1, x2, y2 = map(int, str.split())
    s = Segment2(Point(x1, y1), Point(x2, y2))
    a.append(s)
    
left0 = min([s.left() for s in a])

for s in a:
    dir = Direction(dx = s.left() - left0)
    s.move(dir)
    print(s)
