#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


N  = 100 # muestras
fs = 10 # Hz

A = 1   # Volts
p = 0   # radianes
f = 1  # Hz

Ts = 1/fs       # tiempo de muestreo

tt1 = [n*Ts  for n in range(N)]
tt2 = np.linspace(0, (N-1)*Ts, N).flatten()
tt3 = np.linspace(0, (N-1)*Ts, N)

tt = tt3
#tt = np.asarray(tt1)

# tt = np.linspace(0, N*ts, N, endpoint=False).flatten()   # grilla de sampleo
# tt = np.linspace(0, (N-1)*Ts, N).flatten()   # grilla de sampleo

signal = A * np.sin(2 * np.pi * f * tt + p)

#plt.xlabel ('Tiempo [s]')
#plt.ylabel ('Amplitud [V]')
#plt.plot(tt, signal)

#plt.show   ()


#%% leakage
import scipy.fftpack as sc

N = 1024
fs = 1024
f0 = 50.52
ts = 1/fs


tt = np.linspace( 0.0 , (N-1)/fs , N )

signal = np.sin( 2 * np.pi * f0 * tt )

#Espectro
spc = sc.fft( signal )

#Espectro Normalizado
spc = np.abs( spc ) * ( 2/N )

half_spc = spc[:N//2]

# Base frecuencial
ff = np.linspace( 0.0 , fs/2 , N/2 )

plt.stem( ff , half_spc )
##plt.plot( tt , signal )
plt.show()