#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Inicialización del Notebook del TP2

import numpy as np
from pandas import DataFrame
from IPython.display import HTML
from scipy import signal as sig

import matplotlib.pyplot as plt
from  matplotlib import patches
from matplotlib.figure import Figure
from matplotlib import rcParams

# Insertar aquí el código para inicializar tu notebook
########################################################
def vertical_flaten(a):
    return a.reshape(a.shape[0],1)

def zplane(b,a,filename=None):
    """Plot the complex z-plane given a transfer function.
    """
    # get a figure/plot
    ax = plt.subplot(111)
    # create the unit circle
    uc = patches.Circle((0,0), radius=1, fill=False, color='black', ls='dashed')
    ax.add_patch(uc)

    # The coefficients are less than 1, normalize the coeficients
    if np.max(b) > 1:
        kn = np.max(b)
        b = b/float(kn)
    else:
        kn = 1

    if np.max(a) > 1:
        kd = np.max(a)
        a = a/float(kd)
    else:
        kd = 1
        
    # Get the poles and zeros
    p = np.roots(a)
    z = np.roots(b)
    k = kn/float(kd)
    
    # Plot the zeros and set marker properties    
    t1 = plt.plot(z.real, z.imag, 'go', ms=10)
    plt.setp( t1, markersize=10.0, markeredgewidth=1.0, markeredgecolor='k', markerfacecolor='g')

    # Plot the poles and set marker properties
    t2 = plt.plot(p.real, p.imag, 'rx', ms=10)
    plt.setp( t2, markersize=12.0, markeredgewidth=3.0, markeredgecolor='r', markerfacecolor='r')

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # set the ticks
    r = 1.5; plt.axis('scaled'); plt.axis([-r, r, -r, r])
    ticks = [-1, -.5, .5, 1]; plt.xticks(ticks); plt.yticks(ticks)

    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)

    return z, p, k

N = 3 
b = (1/N)*np.ones(N)
# a = np.array([1,0,0])

ww, hh = sig.freqz(b , 1)
ww = ww

plt.figure(1 , figsize=(16,3) )
plt.subplot(1, 2, 1)
plt.plot(ww, abs(hh))
plt.title('N=3')
plt.xlabel('rad')
plt.ylabel('Modulo')

plt.subplot(1, 2, 2)
plt.plot( ww , np.unwrap(np.angle(hh)) )
plt.title('N=3')
plt.xlabel('rad')
plt.ylabel('angulo[rad]')
plt.show()

fig = plt.figure()
z,p,k=zplane(b,1)


