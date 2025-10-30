import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Если casefold=True — привести к casefold, 
    eсли yo2e=True — заменить все ё/Ё на е/Е,
    убрать невидимые управляющие символы → заменить на пробелы, схлопнуть пробелы в один.
    """

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
    """
    разбить на «слова» по небуквенно-цифровым разделителям.
    В качестве слова считаем последовательности символов \w + дефис внутри слова.
    числа считаем словами
    """
    pattern = r'\b[\w]+(?:-[\w]+)*\b'
    return re.findall(pattern, text)

print("tokenize")
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Подсчитать частоты, вернуть словарь
    """  
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
    """
    Вернуть топ-N по убыванию частоты; при равенстве — по алфавиту слова
    """
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

print("top_n")
print(top_n({'a': 3, 'b': 2, 'c': 1}, n=2))
print(top_n({"aa":2,"bb":2,"cc":1}, n=2))