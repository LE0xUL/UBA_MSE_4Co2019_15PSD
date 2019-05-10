#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: larsul
"""
#%% 3.a

import numpy as np
import scipy.fftpack as sc
import matplotlib.pyplot as plt

N = 1024
fs = 1024
f0 = fs//4
ts = 1/fs
fd = np.array( [0.0 , 0.01 , 0.25 , 0.5] )
numFreq = fd.size

# Base Temporal
tt = np.linspace( 0.0 , (N-1)*ts , N )
# Base frecuencial
ff = np.linspace( 0.0 , fs/2 , N/2 )

# Para almacenar los espectros
half_spc = np.zeros(( numFreq , ff.size ))

#calcula Los 4 Espectros
for i in range( numFreq ):
    signal = np.sin( 2 * np.pi * (f0 + fd[i]) * tt )
    #Espectro
    spc = sc.fft( signal )
    #Espectro Normalizado
    spc = np.abs( spc ) * ( 2/N )
    # La mitad del Espectro
    half_spc[i] = spc[:N//2]

#dibuja Los 4 Espectros
for i in range( numFreq ):
    plt.figure(i+1)
    plt.stem( ff , half_spc[i] )
    #plt.plot( tt , signal )
    plt.title( str(f0 + fd[i]) )
    plt.xlabel( 'Frec [Hz]' )
    plt.ylabel( 'X(f)' )
    plt.show()


tablaRes = np.zeros(( numFreq ,3)) ## numFreq filas X 3 columnas

# Encuentra valor |X(f0)|
for i in range( numFreq ):
    tablaRes[i][0] = half_spc[i][ f0 ]
    tablaRes[i][0] = round( tablaRes[i][0] , 5 )
#    tablaRes[i][0] = float("{0:.4f}".format( half_spc[i][int(f0)] ))

# Encuentra valor |X(f0+1)|
for i in range( numFreq ):
    tablaRes[i][1] = half_spc[i][ f0+1 ]
    tablaRes[i][1] = round( tablaRes[i][1] , 5 )

# Encuentra valor sum |X(f)|**2
for i in range( numFreq ):
    X2 = np.power( half_spc[i] , 2)
    tablaRes[i][2] = X2.sum() - half_spc[i][ f0 ]**2
    tablaRes[i][2] = round( tablaRes[i][2] , 5 )
    
#%% 3.b
Mj = np.array([ N//10 , N , N*10 ])

signal05 = np.sin( 2 * np.pi * (f0 + 0.5 ) * tt )

#calcula Los 3 Espectros
for i in range( Mj.size ):
    tt_zeros = np.linspace( 0.0 , (N + Mj[i] - 1)*ts , N + Mj[i] )
    ff_zeros = np.linspace( 0.0 , fs/2 , (N + Mj[i])/2 )
    
    #Señal
    signal_zeros = np.zeros( N + Mj[i] )
    signal_zeros[:N] = signal05
    
    #Espectro
    spc_zeros = sc.fft( signal_zeros )
    spc_zeros = np.abs( spc_zeros ) * ( 2/(N + Mj[i]) )  #Espectro Normalizado
    half_spc_zeros = spc_zeros[:(N + Mj[i])//2]    # La mitad del Espectro

    plt.figure(i+1 , figsize=(16,3) )

    # Dominio Temporal
    plt.subplot(1, 2, 1)
    plt.stem( tt_zeros , signal_zeros )
    plt.title( "Padding Mj = " + str(Mj[i]) )
    plt.xlabel( 'time' )

    # dominio espectral
    plt.subplot(1, 2, 2)
    plt.stem( ff_zeros , half_spc_zeros )
    #plt.plot( tt , signal )
    plt.title( "Padding Mj = " + str(Mj[i]) )
    plt.xlabel( 'Frec [Hz]' )
    plt.show()

#%% 3.e

Mj = np.array([ 0 , N//10 , N , N*10 ])

res3e = np.zeros(4)

#calcula el maximo
for i in range( Mj.size ):
    tt_zeros = np.linspace( 0.0 , (N + Mj[i] - 1)*ts , N + Mj[i] )
    ff_zeros = np.linspace( 0.0 , fs/2 , (N + Mj[i])/2 )
    
    #Señal
    signal_zeros = np.zeros( N + Mj[i] )
    signal_zeros[:N] = signal05
    
    #Espectro
    spc_zeros = sc.fft( signal_zeros )
    spc_zeros = np.abs( spc_zeros ) * ( 2/(N + Mj[i]) )  #Espectro Normalizado
    half_spc_zeros = spc_zeros[:(N + Mj[i])//2]    # La mitad del Espectro
    
    maxFreq = ff_zeros[ np.argmax( half_spc_zeros ) ]
    
    res3e[i] = (maxFreq/(f0+0.5))*100-100


