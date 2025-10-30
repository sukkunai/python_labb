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
def min_max(nums):
    if isinstance(nums, list) and len(nums) != 0 and all(isinstance(element, (int, float)) for element in nums):
        return min(nums), max(nums)
    return 'ValueError'

print('min_max')
print(min_max([3, -1, 5, 6, 0]))
print(min_max([52]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([2.5, -2, 2.1, 3.1]))

def unique_sorted(nums):
    if isinstance(nums, list) and len(nums) != 0 and all(isinstance(element, (int, float)) for element in nums):
        return sorted(set(nums))
    return nums

print('unique_sorted')
print(unique_sorted([3, 2, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.6, 2.4, 0]))

def flatten(mat):
    if isinstance(mat, (list, tuple)) and len(mat) != 0 and all(isinstance(element, (list, tuple)) for element in mat):
        result = []
        for element in mat:
            result.extend(element)
        return result
    return 'TypeError'

print('flatten')
print(flatten([[2, 3], [4, 5]]))
print(flatten(([2, 3], (4, 5, 6))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "gg"]))
```
![Картинка 1](./images/lab02/arrays.png)

### Задание B
```python
def transpose(mat):
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


def row_sums(mat):
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


def col_sums(mat):
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
def format_record(rec):
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

## Лабораторная работа 3
### Задание A
```python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    result = text
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        result = result.casefold()
    result = re.sub(r'\s+', ' ', result)
    return result.strip()

print("normalize")
print(normalize('ПрИвЕт\nМИр\t'))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize('  двойные   пробелы  '))

def tokenize(text: str) -> list[str]:

    pattern = r'\b[\w]+(?:-[\w]+)*\b'
    return re.findall(pattern, text)

print("tokenize")
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:

    freq_dict = {}  
    for token in tokens:  
        if token in freq_dict:  
            freq_dict[token] += 1  
        else:  
            freq_dict[token] = 1  
    return freq_dict  

print("count_freq")
print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

print("top_n")
print(top_n({'a': 3, 'b': 2, 'c': 1}, n=2))
print(top_n({"aa":2,"bb":2,"cc":1}, n=2))
```

![Картинка 1](./images/lab03/text.png)

### Задание B
```python
import sys
sys.path.append('C:/Users/79032/Desktop/PYTHON_LAB/python_labb')
from scr.lib.moduls import normalize, tokenize, count_freq, top_n

a = sys.stdin.read()

norm = normalize(a)
token = tokenize(norm)
print("Всего слов:", len(token))

count = count_freq(token)
print("Уникальных слов:", len(count))

top = top_n(count)
print("Топ-5:")

for element in top:
    print(element[0], ":", element[1])
```

![Картинка 2](./images/lab03/text_stats.png)

## Лабораторная работа 4
### Задание A
```python
import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    with open(path, 'r', encoding=encoding) as file:
            return ' '.join(file.read().replace("\n", ' ').split())
    
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    
    p = Path(path)
    rows = list(rows)
    
    if rows:
        expected_length = len(rows[0])
        for r in rows:
            if len(r) != expected_length:
                raise ValueError("Все строки должны иметь одинаковую длину")
            
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f,  delimiter=',')
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

#мини тест
import sys
sys.path.append('C:/Users/79032/Desktop/PYTHON_LAB/python_labb')
from io_txt_csv import read_text, write_csv

txt = read_text("C:/Users/79032/Desktop/PYTHON_LAB/python_labb/data/lab04/input.txt")  # должен вернуть строку
f_csv = write_csv([("word","count"),("test",3)], "C:/Users/79032/Desktop/PYTHON_LAB/python_labb/data/lab04/check.csv")  # создаст CSV

print(txt)
print("="*20)
print(f_csv)
```
![Картинка 1](./images/lab04/mini_test.png)


### Задание B
```python
import sys
from pathlib import Path

current_dir = Path(__file__).parent
project_root = current_dir.parent.parent 
sys.path.append(str(project_root / 'scr' / 'lib'))
from moduls import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv


def console(text):
    tokens = tokenize(normalize(text))
    top = top_n(count_freq(tokens))
    output = f"Всего слов: {len(tokens)}"
    output += f"\nУникальных слов: {len(set(tokens))}"
    output += "\nТоп-5:"
    for word, count in top:
        output += f"\n{word}:{count}"
    return output


def from_file_to_text(path, encoding='utf-8'):
    return read_text(path, encoding=encoding)

def frequencies_from_text(text: str) -> dict[str, int]: 
    token = top_n(count_freq(tokenize(normalize(text))))
    return token

def text_to_csv(rows, path=str(project_root / 'data' / 'lab04' / 'report.csv'), header=("word", "count")):
    return write_csv(rows, path=path, header=header)

text_content = from_file_to_text(str(project_root / 'data' / 'lab04' / 'input.txt'))
text_to_csv(frequencies_from_text(text_content))
print(console(text_content))
```
![Картинка 2](./images/lab04/text_report.png)

