import math
from true_math import my_divide as my_t
from fake_math import my_divide as my_f

a1, b1 = 154, 23
a0, b0 = 245, 0
resultT1 = my_t(a1, b1)
resultT0 = my_t(a0, b0)
resultF1 = my_f(a1, b1)
resultF0 = my_f(a0, b0)
print(f'Фейковая математика при делении {a1} на {b1} даст: {resultF1}')
print(f'Истинная математика при делении {a1} на {b1} даст то же самое: {resultT1}')
if b0==0:
    print(f'Фейковая математика при делении {a0} на {b0} даст ошибку - {resultF0}')
    print(f'А истинная математика при делении {a0} на {b0} даст бесконечность ({resultT0})')
