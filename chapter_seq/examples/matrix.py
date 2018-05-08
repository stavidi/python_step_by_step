n = int(input())
m = []
for i in range(n):
    line = input()
    print('--%s--' % line)
    m.append(list(map(int, line.split())))

mT = zip(*m)
print(*mT)
    
mT = [list(r) for r in zip(*m)]
print(*mT)

print(10/0)     # должно привести к ошибке Divizion by zero
