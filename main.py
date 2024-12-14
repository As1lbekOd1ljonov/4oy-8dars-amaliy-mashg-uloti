# vazifa 1
from collections import namedtuple

sportchilar = [
    {"name": "Toxir", "sport_turi": "Boks", "yutuqlari": "12"},
    {"name": "Sobir", "sport_turi": "Boks", "yutuqlari": "15"},
    {"name": "Jobir", "sport_turi": "Boks", "yutuqlari": "13"},

]

Sport = namedtuple("Sport", ["name", "sport_turi", "yutuqlari"])

sport = [Sport(name=c["name"], sport_turi=c["sport_turi"], yutuqlari=int(c["yutuqlari"])) for c in sportchilar]

max_yutuqlar = max(sport, key=lambda c: c.yutuqlari)

print(f"Eng kop qutuqli sportchi: {max_yutuqlar.name }, Yutuqlar soni: {max_yutuqlar.yutuqlari}")

# ============================================================================

# vazifa 2
my_list = [10, 20, 30, 40, 50]
ortacha = sum(my_list) / len(my_list)
print("Ro'yxatdagi elementlarning o'rtacha qiymati:", ortacha)

# ============================================================================

# vazifa 3
def kvadrat_sonlar(start, stop):
    for num in range(start, stop):
        yield num ** 2

for kvadrat in kvadrat_sonlar(1, 10 + 1):
    print(kvadrat)

# ============================================================================

# vazifa 4
from typing import Iterable

string = input("Matn kiritin: ")

class Unli_harflar:
    def __init__(self, text: Iterable):
        self.text = text
        self.index = 0
        self.unli = "aioue"

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1
            if char in self.unli:
                return char
        raise StopIteration("iterable qolmadi!!!")


for i in Unli_harflar(string):
    print(i)

# ============================================================================

# vazifa 5
def juft_sonlar(start, stop):
    for num in range(start, stop):
        if num % 2 == 0:
            yield num


for juft in juft_sonlar(1, 100 + 1):
    print(juft)

# ============================================================================

# vazifa 6
def len_text(text):
    def uzunlik():
        nonlocal text
        len_text = len(text)
        return len_text
    return uzunlik

text = input("Matn kiritin: ")
len_matn = len_text(text)
print(len_matn())