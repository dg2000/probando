import numpy as np

data = np.loadtxt("monthrg.dat")
fecha = data[:,0] + (data[:,1]-1)/12.0
manchas = data[:,3]
ii = fecha>1900

salida = np.array([fecha[ii], manchas[ii]])
np.savetxt("fecha_manchas.dat", salida.T)
