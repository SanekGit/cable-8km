
# coding: utf-8

## *Упрощенная модель кабеля (заглушка)

## Зависимости

# In[1]:

import math
import numpy


# ![Общая схема кабеля](http://pandia.ru/text/78/068/images/image002_135.gif)

## Параметры

# In[2]:

# Длина кабеля
LEN = 5*1000

print "Длина кабеля = {0}км".format(LEN/1000)

# Удельное затухание
ATTm = 0.001
# Затухание
ATT = LEN*ATTm

print "Удельное затухание = {0}Дб/м".format(ATTm)
print "Затухание = {0}Дб".format(ATT)

# Амплитуда шума
NOISE_A = 0.01

print "Амплитуда шума = {0}".format(NOISE_A)


## Функция кабеля

# In[5]:

"""
@signal - сигнал
return - (список частот, список амплитуд)
"""
def cable(signal):
    k = 10**(ATT/10)
    return (1.0/k)*(signal + noise(len(signal)))

"""
Белый шум
@n - кол-во отсчётов
@amp - амплитуда
"""
def noise(n, amp=NOISE_A):
    return amp*(2*numpy.random.random(n) - 1)

