# Словари dict

## Вспомним списки (list)

В списке (list) индекс (номер) - целое число. Номера начинаются с 0. Элементы в списке идут по порядку. Порядок сам не меняется. В список можно добавить элемент или удалить. Можно изменить элемент. Можно отсортировать список или перемешать элементы.

Использование списка:
```python
>>> Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
>>> Days[0]
'Sunday'
>>> Days[1]
'Monday'
```
Хочется получить обратное соответствие. По названию дня недели найти его номер. Можно функцией index найти число, но это долго. Хочется получать быстро так: 

```python
>>> Days['Sunday']
0
>>> Days['Monday']
1
```
Для этого используют словарь (dictionary). 

## Словарь

Пара - это 2. Пара носков. Пара ботинок. Пара луж. Пара рук. Много пар обуви.

Запишем для людей как зовут человека -> какой у него рост. Ключ - как зовут человека. Все люди разные. Какой рост - значение. Рост разных людей может быть одинаковый.

Словарь (dict) - это много пар ключ (key) и значение (value).  

* Ключ и значение вместе называют **item** (пара, элемент словаря)
* **Ключ должен быть уникальным**. Не может быть 2 одинаковых ключей в одном словаре.
* Ключ должен быть **неизменяем** (число, строка, turple - неизменяемы, могут быть ключом; list, set - изменяемы, не могут быть ключом).
* **Значением** может быть все, что угодно: None, число, строка, список, еще один словарь.

Создадим словарь день недели (ключ) - его порядковый номер (значение). Получать по ключу его значение - быстро: 

```python
Days = {
    'Sunday': 0,
    'Monday': 1,
    'Tuesday': 2,
    'Wednessday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6
}
>>> Days['Sunday']          # взять в словаре Days значение по ключу 'Sunday'
0
>>> Days['Monday']
1
>>> Days['Yesterday']       # такого ключа нет в словаре, получили ошибку KeyError
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'Yesterday'
```

 В словарь можно добавлять элементы и удалять их. 
```python
>>> Days['Yesterday'] = -1     # добавили в словарь Days пару ключ 'Yesterday' -> значение -1
>>> Days['Yesterday']          # взять в словаре значение по ключу 'Yesterday' (теперь оно есть)
-1
```

Ключ должен быть уникальным, значения могут совпадать. 
```python
>>> Days['Tomorrow'] = -1
>>> Days['Yesterday'] == Days['Tomorrow']
True
```

Значение в паре можно изменить. 

```python
>>> Days['Tomorrow']
-1
>>> Days['Tomorrow'] = -2
>>> Days['Tomorrow']
-2
```

## Создание словаря

Пустой словарь: 
```python
d1 = dict()
d2 = {}       # вот почему {} нельзя использовать для создания пустого множества, только set()
```
Создадим словарь страна - столица: 

```python
capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington', 'Myanmar':'Naypyidaw', 'Mongolia':'Ulaanbaatar', 'China':'Beijing'}
capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington', )
capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
```
Пишем красиво: 
```python
capitals = {
    'Russia': 'Moscow', 
    'Ukraine': 'Kiev', 
    'USA': 'Washington', 
    'Myanmar':'Naypyidaw', 
    'Mongolia':'Ulaanbaatar', 
    'China':'Beijing'
}
```
##  dict comprehensions 

Можно использовать dict comprehensions при создании словаря: 
```python
cities = ["Moscow", "Kiev", "Washington"]
states = ["Russia", "Ukraine", "USA"]
capitalsOfState = {state: city for city, state in zip(cties, states)}
```
Или с числами: 
```python
square1 = {x : x*x for x in range(10) }                             # dict comprehensions 
square2 = {0=0, 1=1, 2=4, 3=9, 4=16, 5=25, 6=36, 7=49, 8=64, 9=81}  # задаем явно пары ключ=значение
```
Удобно, если нужно вывернуть словарь "наоборот": 

```python
>>> StateByCapital = {CapitalsOfState[state]: state for state in CapitalsOfState}
>>> stateByCapital
{'Kiev': 'Ukraine', 'Moscow': 'Russia', 'Washington': 'USA'}
```
 И с числами: 
```python
sqrts = {square1[x]:x for x in square1}
```
 Этот код будет работать чуть-чуть быстрее: 

```python
sqrts2 = {v:k for k,v in square1.items()}
```

##  Операции над словарем 

| Операция над словарем А |	Значение |
|---|----|
| value = A[key] | Получение элемента по ключу. Если элемента с заданным ключом в словаре нет, то возникает исключение KeyError. |
| value = A.get(key) | Получение элемента по ключу. Если элемента в словаре нет, то get возвращает None. |
| value = A.get(key, default_value) | То же, но вместо None метод get возвращает default_value. |
| key in A | Проверить принадлежность ключа словарю. |
| key not in A | То же, что not key in A. |
| A[key] = value | Добавление нового элемента в словарь или изменяет старое значение на value |
| del A[key] | Удаление пары ключ-значение с ключом key. Возбуждает исключение KeyError?, если такого ключа нет. |
| if key in A:<br/>  del A[key] |	Удаление пары ключ-значение с предварительной проверкой наличия ключа. |
| try:<br/>  del A[key]<br/>except KeyError:<br/>  pass |	Удаление пары ключ-значение с перехватыванием и обработкой исключения. |
| value = A.pop(key) | Удаление пары ключ-значение с ключом key и возврат значения удаляемого элемента. Если такого ключа нет, то возбуждается KeyError. |
| value = A.pop(key, default_value) | То же, но вместо генерации исключения возвращается default_value. |
| A.pop(key, None) | Это позволяет проще всего организовать безопасное удаление элемента из словаря. |
| len(A) | Возвращает количество пар ключ-значение, хранящихся в словаре. |
| A.keys() | Возвращает список ключей |
| A.values() | Возвращает список значений (порядок в нем такой же, как для списка ключей) |
| A.items() | Возвращает список пар ключ, значение  |

##  Перебор словаря 

**При переборе словаря порядок ключей и пар может быть любой. Порядок может измениться со временем (а может остаться прежним).**

```python
In [12]: capital = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington',
    ...:  'Myanmar':'Naypyidaw', 'Mongolia':'Ulaanbaatar', 'China':'Beijing'}

In [13]: capital
Out[13]:
{'China': 'Beijing',
 'Mongolia': 'Ulaanbaatar',
 'Myanmar': 'Naypyidaw',
 'Russia': 'Moscow',
 'USA': 'Washington',
 'Ukraine': 'Kiev'}
```
 По ключам: 

```python
In [14]: for s in capital:
    ...:     print(s, capital[s])
    ...:
China Beijing
Mongolia Ulaanbaatar
Ukraine Kiev
Russia Moscow
USA Washington
Myanmar Naypyidaw
```
 Можно явно написать, что по списку ключей 

```python
In [15]: for s in capital.keys():
    ...:     print(s, capital[s])
China Beijing
Mongolia Ulaanbaatar
Ukraine Kiev
Russia Moscow
USA Washington
Myanmar Naypyidaw
```
 и отсортировать ключи: 
 
```python
In [18]: for s in sorted(capital.keys()):
    ...:     print(s, capital[s])
China Beijing
Mongolia Ulaanbaatar
Myanmar Naypyidaw
Russia Moscow
USA Washington
Ukraine Kiev
```
 Только значения: 
 
```python
In [19]: for c in capital.values():
    ...:     print(c)
    ...:
Beijing
Ulaanbaatar
Kiev
Moscow
Washington
Naypyidaw
```

(да, capital.values() тоже можно отсортировать!)

Если нам в цикле будет нужен и ключ, и значение, лучше перебирать по парам: 

```python
In [20]: for s, c in capital.items():
    ...:     print(s, c)
China Beijing
Mongolia Ulaanbaatar
Ukraine Kiev
Russia Moscow
USA Washington
Myanmar Naypyidaw
```
Пары тоже можно отсортировать: 
```python
In [21]: for s, c in sorted(capital.items()):
    ...:     print(s, c)
China Beijing
Mongolia Ulaanbaatar
Myanmar Naypyidaw
Russia Moscow
USA Washington
Ukraine Kiev
```

 В обратном порядке reverse=True: 
 
```python
In [22]: for s, c in sorted(capital.items(), reverse=True):
    ...:     print(s, c)
Ukraine Kiev
USA Washington
Russia Moscow
Myanmar Naypyidaw
Mongolia Ulaanbaatar
China Beijing
```
