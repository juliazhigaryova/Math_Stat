# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

import numpy as np
n = 144
m = 70
p = 0.5
lambda_ = n * p

P = (lambda_**m / np.math.factorial(m)) * np.exp(-lambda_)
print(P)

# Ответ: 0.046309172162262796
