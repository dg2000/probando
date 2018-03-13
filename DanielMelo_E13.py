import numpy as np

import matplotlib.pyplot as plt

import math

from scipy.fftpack import fft, fftfreq


archivo = np.loadtxt("monthrg.dat")


anos = archivo[:, 0]

dias = archivo[:, 1]

mediciones = archivo[:, 2]

manchas = archivo[:, 3]

dispersion = archivo[:, 4]



ii = manchas > -1

anos = anos[ii]

manchas = manchas[ii]



x = np.linspace(-2*np.pi+0.2 , 2*np.pi, 1000)




def fourier(entrada, salida):

    real = np.zeros(len(entrada))

    img = np.zeros(len(entrada))

    for k in range(len(entrada)-1):

        for n in range(len(entrada)-1):

            real[k] = real[k] + salida[n]*np.cos(2*np.pi*n*k/len(entrada))

            img[k] = img[k] + salida[n]*np.sin(-2*np.pi*n*k/len(entrada))


    return 2*real/len(entrada), 2*img/len(entrada)





            

#norma = (fourier(x, y)[0]**2.0   +  fourier(x, y)[1]**2.0)**(1.0/2.0)



n = len(manchas) # number of point in the whole interval

dt = 1.0/12.0
t = ii

manchas = manchas -35.0

fft_x = fft(manchas)/n

freq = fftfreq(n, dt)


plt.plot(freq,abs(fft_x))

plt.xlim(0.01, 0.2)




ind = np.where((freq > 0.05))[0]

freq = freq[ind]

fft_x = fft_x[ind]

hola = np.where( (abs(fft_x) > 8.0))[0]

print "El periodo de oscilacion de los datos es ", 1/freq[hola][0], " en years"




