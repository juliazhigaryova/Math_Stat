# В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

total = combinations(15, 3)
positive = combinations(9, 3)
p = positive / total
print(p)

# Ответ: вероятность = 18%
