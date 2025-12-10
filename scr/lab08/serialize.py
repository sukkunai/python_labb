import json
from models import Student

def students_to_json(students, path):
    data = []
    for elm in students:
        data.append(elm.to_dict())

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    result = []
    for elm in data:
        try:
            student = Student.from_dict(elm)
            result.append(student)
        except ValueError:
            continue

    return result
