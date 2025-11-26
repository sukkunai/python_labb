def format_record(rec):
    if len(rec[0]) == 0 or len(rec[1]) == 0:
        return "ValueError"
    if type(rec[2]) is not float:
        return "TypeError"
    if isinstance(rec, tuple):
        if (
            isinstance(rec[0], str)
            and isinstance(rec[1], str)
            and isinstance(rec[2], float)
        ):
            name = rec[0].split()
            full_name = name[0][0].upper() + name[0][1:] + " "
            for initials in name[1:]:
                full_name += initials[0].upper() + "."
            return f'{full_name}, гр. {rec[1]}, GPA {"{:.2f}".format(rec[2])}'


print(format_record(("Анисимова Олеся Сергеевна", "BIVT-25", 4.6)))
print(format_record(("Сидорова Анна", "IKBO-12", 5.0)))
print(format_record(("Константинов Константин Константинович", "BIVT-12", 5.0)))
print(format_record(("  анисимова  олеся   сергеевна ", "IT-01", 4.999)))
