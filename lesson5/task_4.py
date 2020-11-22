# Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?
import pandas as pd

# H0 = вес пачки  = 200, m=m0
# H1 =  вес пачки != 200, m != m0
# a = 0.01
# Используем t-критерий

x = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
a = pd.DataFrame(x)
height_std = a.std(ddof=1)  # 4.45
m = a.mean()                # 198.5
Tt = 3.250
Tn = (198.5 - 200) / 4.45/10
Tn = -0.033

# Ответ: Tn < Tt, значит H0 верна на уровне значимости а = 0.01
