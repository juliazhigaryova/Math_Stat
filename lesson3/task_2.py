# В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
# Какова вероятность того, что 3 мяча белые?
from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# 1. из первого ящика вынимаем 0 белых мячей, а из второго 3 мяча белых + 1 черный

p1 = (combinations(5,0) * combinations(3,2)) / combinations(8,2) * (combinations(5,3) * combinations(7,1)) / combinations(12,4)
# 0.015151515151515152

# 2. из первого ящика вынимаем 1 белый+ 1черный и из второго 2 белых + 2 черных
p2 = (combinations(5, 1) * combinations(3, 1)) / combinations(8, 2) * (combinations(5, 2) * combinations(7, 2)) / combinations(12, 4)
# 0.22727272727272727

# 3. из первого ящика вынимаем 2 белых и из второго 1 белый + 3 черных
p3 = (combinations(5, 2) * combinations(3, 0)) / combinations(8, 2) * (combinations(5, 1) * combinations(7, 3)) / combinations(12, 4)
# 0.12626262626262627

p = p1 + p2 + p3
# 0.36868686868686873
