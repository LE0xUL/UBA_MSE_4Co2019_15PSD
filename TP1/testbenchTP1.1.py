# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a test Bench script file for TP1  of 15.SPD
"""

# Leonardo Urrego, University of Buenos Aires, AR
# Módulos para Jupyter
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib as mpl
#%%  Inicialización de librerías
# Setup inline graphics: Esto lo hacemos para que el tamaño de la salida,
# sea un poco más adecuada al tamaño del documento
mpl.rcParams['figure.figsize'] = (10,10)

import matplotlib.pyplot as plt
#import pdsmodulos as pds

#%% Esto tiene que ver con cuestiones de presentación de los gráficos,
# NO ES IMPORTANTE
fig_sz_x = 14
fig_sz_y = 13
fig_dpi = 80 # dpi

fig_font_family = 'Ubuntu'
fig_font_size = 16

plt.rcParams.update({'font.size':fig_font_size})
plt.rcParams.update({'font.family':fig_font_family})

#%% Funcion que genera senoidal
def genSen( fs , f0 , N , A , phase ):
    """
    brief:  Generador de señales senoidal, con argumentos

    fs:     frecuencia de muestreo de la señal [Hz]
    N:      cantidad de muestras de la señal a generar
    f0:     frecuencia de la senoidal [Hz]
    A:      amplitud pico de la señal [V]
    phase:  fase de la señal sinusoidal [rad]

    como resultado la señal devuelve:

    signal: senoidal evaluada en cada instante
    tt:     base de tiempo de la señal
    """

    # tiempo de muestreo
    Ts = 1/fs

    # Se crea una lista para la base de tiempo y se convierte en array numerico
    tt =   np.asarray( [n/fs  for n in range(N)] )

    #Se Genera la Señal
    signal = A * np.sin(2 * np.pi * f0 * tt + phase)

    return tt , signal

# Main program starts here
#%% Definiciones iniciales

# NO modifiques este bloque
############################

#N  = 1000 # muestras
#fs = 1000 # Hz


#%% 1.a 

#A = 1 # Volts
#p = 0 # radianes
#f = 10   # Hz

#[ tt , signal ] = genSen( fs , f , N , A , p )


#titleImg = 'Señal Senoidal a ' + str(f) + 'Hz'

#%% Presentación gráfica de los resultados
#plt.figure(1)
#plt.plot( tt , signal )
#plt.title( titleImg )
#plt.xlabel( 'Tiempo [Seg]' )
#plt.ylabel( 'Amplitud [V]' )
#    plt.grid(which='both', axis='both')
#plt.show()


#%% 3.a
import scipy.fftpack as sc

N = 1024
fs = 1024
f0 = fs/4
ts = 1/fs
fd = np.array( [0.0 , 0.01 , 0.25 , 0.25] )

# Base Temporal
tt = np.linspace( 0.0 , (N-1)/fs , N )
# Base frecuencial
ff = np.linspace( 0.0 , fs/2 , N/2 )

#calcula Los 4 Espectros
for i in range( len(fd) ):
    signal = np.sin( 2 * np.pi * (f0 + fd[i]) * tt )
    #Espectro
    spc = sc.fft( signal )
    #Espectro Normalizado
    spc = np.abs( spc ) * ( 2/N )
    # La mitad del Espectro
    half_spc = spc[:N//2]
    
    plt.figure(i+1)
    plt.stem( ff[:100] , half_spc[:100] )
    #plt.plot( tt , signal )
    plt.title( str(f0 + fd[i]) )
    plt.xlabel( 'Frec [Hz]' )
    plt.ylabel( 'FFT' )
    plt.show()




#plt.figure(i+1)
#    plt.stem( ff , half_spectrum_abs[i])
#    plt.title('FFT: $F_s/4$ + ' + str(Fd[i][0]) )
#    plt.xlabel('frecuencia [Hz]')
#    plt.ylabel('|F(w)|')
#    plt.show()































