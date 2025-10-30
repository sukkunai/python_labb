import sys
sys.path.append('C:/Users/79032/Desktop/PYTHON_LAB/python_labb')
from io_txt_csv import read_text, write_csv

txt = read_text("C:/Users/79032/Desktop/PYTHON_LAB/python_labb/data/lab04/input.txt")  # должен вернуть строку
f_csv = write_csv([("word","count"),("test",3)], "C:/Users/79032/Desktop/PYTHON_LAB/python_labb/data/lab04/check.csv")  # создаст CSV

print(txt)
print("="*20)
print(f_csv)