# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз.
# Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
from math import factorial
import numpy as np
n = 100
k = 85
p = 0.8

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

c = combinations(n, k)

# биномиальное распределение

P = c * p**k * 0.2**15

# Ответ: 0.048061793700746556
