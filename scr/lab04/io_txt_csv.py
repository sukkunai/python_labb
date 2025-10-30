import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку 
    + обработка ошибок + возможность выбора кодировки
    """

    with open(path, 'r', encoding=encoding) as file:
            return ' '.join(file.read().replace("\n", ' ').split())
    

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Создать/перезаписать CSV с разделителем "," + Если передан header, записать его первой строкой 
    + Проверить, что каждая строка в rows имеет одинаковую длину (иначе ValueError)
    """
     
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


txt = read_text("C:/Users/79032/Desktop/PYTHON_LAB/python_labb/data/lab04/input.txt")  # должен вернуть строку
f_csv = write_csv([("word","count"),("test",3)], "C:/Users/79032/Desktop/PYTHON_LAB/python_labb/data/lab04/check.csv")  # создаст CSV

print(txt)
print("="*20)
print(f_csv)


