import sys
from pathlib import Path

current_dir = Path(__file__).parent
project_root = current_dir.parent.parent  # поднимаемся на два уровня вверх
sys.path.append(str(project_root / "scr" / "lib"))
from moduls import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv


def console(text):  # вывод в консоль из файла input.txt
    tokens = tokenize(normalize(text))
    top = top_n(count_freq(tokens))
    output = f"Всего слов: {len(tokens)}"
    output += f"\nУникальных слов: {len(set(tokens))}"
    output += "\nТоп-5:"
    for word, count in top:
        output += f"\n{word}:{count}"
    return output


def from_file_to_text(
    path, encoding="utf-8"
):  # перевод содержимого файла input.txt в единую строку
    return read_text(path, encoding=encoding)


def frequencies_from_text(
    text: str,
) -> dict[str, int]:  # токенизация, нормализация, счет частоты слов из ЛР3
    token = top_n(count_freq(tokenize(normalize(text))))
    return token


def text_to_csv(
    rows,
    path=str(project_root / "data" / "lab04" / "report.csv"),
    header=("word", "count"),
):
    # запись в csv
    # если файл input.txt - пустой, то в файле report.csv только заголовок
    return write_csv(rows, path=path, header=header)


text_content = from_file_to_text(str(project_root / "data" / "lab04" / "input.txt"))
text_to_csv(frequencies_from_text(text_content))
print(console(text_content))
