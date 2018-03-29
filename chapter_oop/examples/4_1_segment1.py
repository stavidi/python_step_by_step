class Segment1(object):
    """Класс Segment1 описывает отрезки на оси Х"""
    
    counter = 0 # еще не было создано ни одной окружности
    
    def __init__(self, start=0, finish=0):
        # Эта функция вызывается, когда мы создаем новый объект класса.
        # self - это название переменной, которая указвает на сам объект.
        self.start = start      # переменная объекта 
        self.finish = finish
        Segment1.counter += 1
        
    @classmethod
    def how_many(cls):
        return cls.counter
        
    def __str__(self):
        return '{} {}'.format(self.start, self.finish)

    def crossed_with(self, other):
        """ Пересекается этот отрезок self с другим отрезком other? """
        if self.finish < other.start or other.finish < self.start:
            return False
        return True
        
    @staticmethod
    def is_crossed(seg1, seg2):
        """ Пересекаются ли отрезки seg1 и seg2? """
        if seg1.finish < seg2.start or seg2.finish < seg1.start:
            return False
        return True
        

# Закончились отступы - закончилось описание класса.
# Классом можно пользоваться:        
def test1():        
    s1 = Segment1(-3.5, 7)      # вызывается __init__(-3.5, 7)
    print(s1.start, s1.finish)  # объект.переменная - к полям можно обратиться по имени через точку

    x = s1.length()         # объект.метод
    print('Длина равна', x)

    print(s1)               # вызывается str(s1), которая вызывает s1.__str__()

    s1.start = 1            # объект.переменная - изменили значение поля start объекта s1
    print(s1)               # 1 7

    s1.move(2)              # передвинули отрезок на +2 по оси Х
    print(s1)               # 3 9

    s2 = Segment1(0, 2.5)   # другой объект класса Segment1, на него ссылается s2
    print(s2)               # 0 2.5

    s2 = s1
    print(s2)               # 3 9 теперь s2 тоже ссылается на отрезок [3, 9], на отрезок [0, 2.5] нет ссылок.

    print(Segment1.__dict__)
    print(s1.__dict__)

def test2():
    s1 = Segment1(2, 5)
    s2 = Segment1(3, 7)
    
    print(s1.crossed_with(s2))          # метод экземпляра класса
    print(Segment1.is_crossed(s1, s2))  # статический метод класса
    
def test3():
    s1 = Segment1(2, 5)
    s2 = Segment1(3, 7)
    
    print(Segment1.how_many())          # вызов метода класса по имени класса
    
if __name__ == '__main__':
    # test2()
    test3()
