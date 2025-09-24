a = input("")
if ',' in a: a = a.replace(',','.')
b = input("")
if ',' in b: b = b.replace(',','.')
floata = float(a)
floatb = float(b)

Sum = floata + floatb
Average = Sum / 2

print(f'sum = {Sum:.2f}; avg = {Average:.2f}')