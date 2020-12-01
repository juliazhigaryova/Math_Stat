# Посчитать коэффициент линейной регрессии при заработной плате (zp),
# используя градиентный спуск (без intercept).

import numpy as np

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

def mse_(B1, y = y, x = x, n = 10):
    return np.sum((B1 * x - y)**2) / n

alpha = 0.000001
n = x.size
B0 = 0


# Сначала число итераций = 10
n_iter = 10

B1 = 0.1
for i in range(n_iter):
    B1 -= alpha * (2 / n) * np.sum((B1 * x - y) * x)
    # print(f'i = {i:{4}};\t B1 = {round(B1, 10)};\t mse = {round(mse_(B1), 12)}')

# Увелиливаем число итераций = 2000
n_iter = 2000

B1 = 0.1
for i in range(n_iter):
    B1 -= alpha * (2 / n) * np.sum((B1 * x - y) * x)
    if (i % 100 == 0):
        print(f'i = {i:{4}};\t B1 = {round(B1, 10)};\t mse = {round(mse_(B1), 12)}')

# при i > 900 B1 и mse не меняются до 10-11-го знаков

print('B0 =', round(B0, 10)) # 0
print('B1 =', round(B1, 10)) # 5.8898204201

print(f'Тогда получаем модель вида y = B1 * x:\n\t y = {round(B1, 10)} * x')
# y = 5.8898204201 * x