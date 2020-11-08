# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# Найти вероятность того, что все карты – крести

total_clubs = int(52 / 4)
positive = combinations(13, 4)
total = combinations(52, 4)
probability = positive / total
print(probability)
# Ответ: Вероятность около 3%

# Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
# 1 туз
# 83300 сочетаний
positive_1 = combinations(4, 1)
other_cards = combinations(51, 3)
c1 = positive_1 * other_cards
print(c1)

# 2 туза
# 7350 сочетаний
positive_2 = combinations(4, 2)
other_cards = combinations(50, 2)
c2 = positive_2 * other_cards
print(c2)

# 3 туза
# 196 сочетаний
positive_3 = combinations(4, 3)
other_cards = combinations(49, 1)
c3 = positive_3 * other_cards
print(c3)

# 4 туза
positive_4 = combinations(4, 4)
other_cards = combinations(48, 1)
c4 = positive_4 * other_cards
print(c4)

# всего сочетаний
# 90894
c = c1 + c2 + c3 + c4
p = c / total
# Ответ: вероятность : около 33%







