
# coding: utf-8

## Зависимости

# In[1]:

import math
import numpy


## Общие функции

# In[26]:

def avg(array):
    return sum(array)/float(len(array))

"""
Преобразует последовательность бит в уровень от -amp до amp
@bit_seq - последовательность бит
@amp - амплитуда модуляции
return - уровень от -amp до amp
"""
def bit_seq_to_level(bit_seq, amp):
    num = sum(map(lambda (i, x): x * 2**i, zip(xrange(len(bit_seq)), bit_seq)))
    max_num = 2**len(bit_seq) - 1
    return -amp*(1.0 - 2.0*num/max_num)

"""
Обратная к @ref bit_seq_to_level функция
return - ближайший уровень
"""
def level_to_bit_seq(level, bit_count, amp):
    levels = numpy.linspace(-amp, amp, 2**bit_count)
    closest_level_index = abs(levels - level).argmin()
    max_num = 2**bit_count - 1
    num = int(round((levels[closest_level_index]/amp + 1.0)*max_num/2.0))
    return [(num >> i) & 1 for i in xrange(bit_count)]

"""
@signal - исходный сигнал
@scale - кол-во отсчётов отмасштабированного/интерполированного сигнала на один отсчёт исходного
return - отмасштабированный/интерполированный сигнал
"""
def scale_signal(signal, scale):
   return numpy.array([signal[i//scale] for i in xrange(scale*len(signal))])

"""
Обратная к @ref scale_signal функция
"""
def unscale_signal(signal, scale):
    return numpy.array([avg(signal[i*scale:(i+1)*scale]) for i in xrange(len(signal)//scale)])

"""
Вычисляет АЧХ сигнала
@signal - сигнал
@sampling_freq - частота дискретизации
return - (список частот, список амплитуд)
"""
def compute_signal_afc(signal, sampling_freq):
    sampling_period = 1.0/sampling_freq
    t = numpy.linspace(0, len(signal)*sampling_period, len(signal))
    afc = 2*abs(numpy.fft.fft(signal)[0:len(t)//2])/len(t)
    freq = numpy.fft.fftfreq(len(t))[0:len(t)//2]*sampling_freq
    return (freq, afc)

