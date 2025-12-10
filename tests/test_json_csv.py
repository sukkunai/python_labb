import pytest
from pathlib import Path
import csv
import json
from scr.lib.json_csv import json_to_csv, csv_to_json

"""позитивчик"""

def test_csv_to_json_basic(tmp_path: Path):
    #Проверка корректной конвертации CSV → JSON
    scr = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    rows = [
        ["name", "age"],
        ["Alice", "22"],
        ["Bob", "25"],
    ]

    with scr.open("w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    csv_to_json(scr, dst)

    data = json.loads(dst.read_text(encoding="utf-8"))

    assert len(data) == 2
    assert data[1]["name"] == "Bob"
    assert set(data[0].keys()) == {"name", "age"}

def test_json_to_csv_basic(tmp_path: Path):
    #Проверка корректной конвертации JSON → CSV
    scr = tmp_path / "people.json"
    dst = tmp_path / "people.csv"

    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]

    scr.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    json_to_csv(scr, dst)

    with dst.open(encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

    assert len(reader) == 2
    assert reader[0]["name"] == "Alice"
    assert set(reader[0].keys()) == {"name", "age"}

"""туда-сюда"""
def test_json_to_csv_roundtrip(tmp_path: Path):
    scr = tmp_path / "people.json"
    mid = tmp_path / "people.csv"
    dst = tmp_path / "people2.json"

    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]

    scr.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    json_to_csv(scr, mid)
    csv_to_json(mid, dst)

    data2 = json.loads(dst.read_text(encoding="utf-8"))

    assert data2 == [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]


def test_csv_to_json_roundtrip(tmp_path: Path):
    scr = tmp_path / "data.csv"
    mid = tmp_path / "data.json"
    dst = tmp_path / "data2.csv"

    rows = [
        ["city", "tsss"],
        ["Moscow", "677554335"],
        ["Paris", "5234521"],
    ]

    with scr.open("w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    csv_to_json(scr, mid)
    json_to_csv(mid, dst)

    with dst.open(encoding="utf-8") as f:
        result = list(csv.DictReader(f))

    assert len(result) == 2
    assert set(result[0].keys()) == {"city", "tsss"}

"""негативчик"""
def test_json_to_csv_empty_file(tmp_path: Path):
    # пустой JSON файл - ValueError
    scr = tmp_path / "bad.json"
    dst = tmp_path / "out.csv"
    scr.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(scr), str(dst))


def test_csv_to_json_empty_file(tmp_path: Path):
    # пустой CSV файл - ValueError
    scr = tmp_path / "bad.csv"
    dst = tmp_path / "out.json"
    scr.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(scr), str(dst))

def test_json_to_csv_missing_file(tmp_path: Path):
    # несуществующий JSON файл - FileNotFoundError
    scr = tmp_path / "no_file.json"
    dst = tmp_path / "out.csv"

    with pytest.raises(FileNotFoundError):
        json_to_csv(scr, dst)

def test_csv_to_json_missing_file(tmp_path: Path):
    # несуществующий CSV файл - FileNotFoundError
    scr = tmp_path / "no_file.csv"
    dst = tmp_path / "out.json"

    with pytest.raises(FileNotFoundError):
        csv_to_json(scr, dst)