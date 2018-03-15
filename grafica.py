import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("fecha_manchas.dat")

plt.plot(data[:,0], data[:,1])

plt.savefig("fecha_manchas.pdf")
