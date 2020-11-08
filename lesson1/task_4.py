# В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


total = combinations(100, 2)
positive = combinations(2, 2)
p = positive / total
print(p)

# Ответ = вероятность около 0,02%
