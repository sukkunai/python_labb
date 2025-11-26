import sys

sys.path.append("C:/Users/79032/Desktop/PYTHON_LAB/python_labb")
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
