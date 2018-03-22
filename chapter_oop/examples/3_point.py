class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({} {})'.format(self.x, self.y)
        
    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """ Меньше та точка, у которой меньше х. При одинаковых x, та, у которой меньше y."""
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x
    
    # другие функции класса: move, dir, dist...

if __name__ == '__main__':
    p0 = Point(3, 5)
    p1 = Point(3, 5)
    p2 = Point(-1, 7)
    p3 = Point(3, 1.17)
    
    print('p0=', p0)       # 3 5
    print('p1=', p1)       # 3 5
    print('p2=', p2)       # -1 7
    print('p3=', p3)       # 3 1.17
    
    print('p0 == p1', p0 == p1) # True
    print('p1 == p2', p1 == p2) # False
    
    print('p0 != p1', p0 != p1) # False
    print('p1 != p2', p1 != p2) # True
    
    print('p2 < p1', p2 < p1)   # True
    print('p1 < p2', p1 < p2)   # False

    print('p3 < p1', p3 < p1)   # True
    print('p1 < p3', p1 < p3)   # False
    
    a = [p0, p1, p2, p3]
    pmin = min(a)
    print('pmin =', pmin)
    
    b = sorted(a)
    print(b)
