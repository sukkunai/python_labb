# python_labb
## Лабораторная работа 1

### Задание 1
```python
name = input("")  
age = int(input(""))  
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![Картинка 1](./images/lab01/ex01.png)

### Задание 2
```python
a = input("")
if ',' in a: a = a.replace(',','.')
b = input("")
if ',' in b: b = b.replace(',','.')
floata = float(a)
floatb = float(b)

Sum = floata + floatb
Average = Sum / 2

print(f'sum = {Sum:.2f}; avg = {Average:.2f}')
```
![Картинка 2](./images/lab01/ex02.png)

### Задание 3
```python
price = input('')
discount = input('')
vat = input('')
base = int(price) * (1 - int(discount)/100)
vat_amount = base * (int(vat)/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f}.', f'НДС: {vat_amount:.2f}.', f'Итого к оплате: {total:.2f}.', sep='\n')
```
![Картинка 3](./images/lab01/ex03.png)

### Задание 4
```python
minutes = input('')
m = int(minutes)
h = m // 60
ost = m % 60
print(f'{h}:{ost}')
```
![Картинка 4](./images/lab01/ex04.png)

### Задание 5
```python
FIO = input('').strip()
FIO2 = ' '.join(FIO.split())
initials = ''.join([w[0].upper() for w in FIO2.split()])
print(f'{initials}.')
print(f'{len(FIO2)}')
```
![Картинка 5](./images/lab01/ex05.png)

### Задание 6
```python
def count_participants():  
    n = int(input(""))
      
    offline = 0  
    online = 0  
      
    for _ in range(n):  
        data = input().split()  
          
        participation_format = data[-1] == 'True'  
         
        if participation_format:  
            offline += 1  
        else:  
            online += 1 
    
    print(f" {offline}", f" {online}", sep=" ")  
  
count_participants()
```
![Картинка 6](./images/lab01/ex06.png)

### Задание 7
```python
ex = "thisisabracadabraHt1eadljjl12ojh."
def res_str(s):
    
    for i, ch in enumerate(s):
        if ch.isupper():
            start = i
            break
    else:
        return None  
    
    for i, ch in enumerate(s):
        if ch.isdigit() and i + 1 < len(s):
            step = (i + 1) - start
            if step <= 0:
                continue
            
            result = []
            pos = start
            while pos < len(s):
                result.append(s[pos])
                if s[pos] == '.':
                    return ''.join(result)
                pos += step
    
    return None
    
print(res_str(ex))
```
![Картинка 7](./images/lab01/ex07.png)

## Лабораторная работа 2

### Задание 1
```python
<<<<<<< HEAD
def min_max(nums):
=======
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
>>>>>>> 6b14d9450f439602e12cb926e62f141b344fa2c6
    if isinstance(nums, list) and len(nums) != 0 and all(isinstance(element, (int, float)) for element in nums):
        return min(nums), max(nums)
    return 'ValueError'

print('min_max')
<<<<<<< HEAD
print(min_max([3, -1, 5, 6, 0]))
print(min_max([52]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([2.5, -2, 2.1, 3.1]))

def unique_sorted(nums):
=======
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
>>>>>>> 6b14d9450f439602e12cb926e62f141b344fa2c6
    if isinstance(nums, list) and len(nums) != 0 and all(isinstance(element, (int, float)) for element in nums):
        return sorted(set(nums))
    return nums

print('unique_sorted')
<<<<<<< HEAD
print(unique_sorted([3, 2, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.6, 2.4, 0]))

def flatten(mat):
=======
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))


def flatten(mat: list[list | tuple]) -> list:
>>>>>>> 6b14d9450f439602e12cb926e62f141b344fa2c6
    if isinstance(mat, (list, tuple)) and len(mat) != 0 and all(isinstance(element, (list, tuple)) for element in mat):
        result = []
        for element in mat:
            result.extend(element)
        return result
    return 'TypeError'

print('flatten')
<<<<<<< HEAD
print(flatten([[2, 3], [4, 5]]))
print(flatten(([2, 3], (4, 5, 6))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "gg"]))
=======
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
>>>>>>> 6b14d9450f439602e12cb926e62f141b344fa2c6
```
![Картинка 1](./images/lab02/arrays.png)

### Задание B
```python
<<<<<<< HEAD
def transpose(mat):
=======
def transpose(mat: list[list[float | int]]) -> list[list]:
>>>>>>> 6b14d9450f439602e12cb926e62f141b344fa2c6
    if len(mat) == 0:
        return []
    if isinstance(mat, list) and all(isinstance(row, list) for row in mat) and all(isinstance(element, (int, float)) for row in mat for element in row):
        row_len = [len(row) for row in mat]
        if len(set(row_len)) != 1:
            return 'ValueError'

        return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

print('transpose')
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))


<<<<<<< HEAD
def row_sums(mat):
=======
def row_sums(mat: list[list[float | int]]) -> list[float]:
>>>>>>> 6b14d9450f439602e12cb926e62f141b344fa2c6
    if len(mat) == 0:
        return []
    if isinstance(mat, list) and all(isinstance(row, list) for row in mat) and all(isinstance(element, (int, float)) for row in mat for element in row):
        row_len = [len(row) for row in mat]
        if len(set(row_len)) != 1:
            return 'ValueError'
        return [sum(element) for element in mat]

print('row_sums')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


<<<<<<< HEAD
def col_sums(mat):
=======
def col_sums(mat: list[list[float | int]]) -> list[float]:
>>>>>>> 6b14d9450f439602e12cb926e62f141b344fa2c6
    if len(mat) == 0:
        return []
    if isinstance(mat, list) and all(isinstance(row, list) for row in mat) and all(isinstance(element, (int, float)) for row in mat for element in row):
        row_len = [len(row) for row in mat]
        if len(set(row_len)) != 1:
            return 'ValueError'
    result = []
    for col_index in range(len(mat[0])):
        sum_col = 0
        for row in mat:
            sum_col += row[col_index]
        result.append(sum_col)
    return result

print('col_sums')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![Картинка 2](./images/lab02/matrix.png)

### Задание C
```python
<<<<<<< HEAD
def format_record(rec):
=======
def format_record(rec: tuple[str, str, float]) -> str:
>>>>>>> 6b14d9450f439602e12cb926e62f141b344fa2c6
    if len(rec[0]) == 0 or len(rec[1]) == 0:
        return 'ValueError'
    if type(rec[2]) is not float:
        return 'TypeError'
    if isinstance(rec, tuple):
        if isinstance(rec[0], str) and isinstance(rec[1], str) and isinstance(rec[2], float):
            name = rec[0].split()
            full_name = name[0][0].upper() + name[0][1:] + ' '
            for initials in name[1:]:
                full_name += initials[0].upper() + '.'
            return f'{full_name}, гр. {rec[1]}, GPA {"{:.2f}".format(rec[2])}'

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
![Картинка 3](./images/lab02/tuples.png)
