
# coding: utf-8

## *Упрощенная модель кабеля (заглушка)

## Зависимости

# In[1]:

import math
import numpy


# ![Общая схема кабеля](http://pandia.ru/text/78/068/images/image002_135.gif)

## Параметры

# In[4]:

# Длина кабеля
LEN = 5*1000

print "Длина кабеля = {0}км".format(LEN/1000)

# Удельное затухание Дб/м
ATTm = 0.005
# Затухание Дб
ATT = LEN*ATTm
# Отношение Ain/Aout
K = 10**(ATT/10)

print "Удельное затухание = {0}Дб/м".format(ATTm)
print "Затухание = {0}Дб".format(ATT)

# Амплитуда шума
NOISE_A = 0.1

print "Амплитуда шума = {0}".format(NOISE_A)


## Функция кабеля

# In[5]:

"""
@signal - сигнал
return - (список частот, список амплитуд)
"""
def cable(signal, noise_amp=NOISE_A):
    return (1.0/K)*(signal + noise(len(signal), noise_amp))

"""
Белый шум
@n - кол-во отсчётов
@amp - амплитуда
"""
def noise(n, amp=NOISE_A):
    return amp*(2*numpy.random.random(n) - 1)

