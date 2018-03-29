class A(object):
    def __init__(self, x):
        self.x = x
        
    def __str__(self):
        return str(self.x)
        
    @classmethod
    def new_A(cls, s):
        t = cls(int(s))
        return t
        
    @staticmethod
    def common_foo(x, k):
        return x * k
        
    def a_foo(self, k):
        self.x = self.common_foo(self.x, k) # через self
        self.x = A.common_foo(self.x, k)    # через им€ класса
    
a1 = A(1)
print('a1 =', a1)

a2 = A.new_A("2")
print('a2 =', a2)

z = A.common_foo(3, 4)  # класс.статический_метод
print('z =', z)

z = a1.common_foo(3, 4) # экземпл€р_класса.статический_метод
print('z =', z)
print('a1 =', a1)

a1.a_foo(5)
print('a1 =', a1)

