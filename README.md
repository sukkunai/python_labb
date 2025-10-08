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