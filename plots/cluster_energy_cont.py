import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import pickle
import numpy as np

with open('data/gauss_cluster_data.pickle','br') as file:
    gauss_cluster_data = pickle.load(file)

x = []
y = []
yerr = []

for key in list(gauss_cluster_data):
    N, beta = key
    energy_mean = gauss_cluster_data[key]['energy_mean']
    energy_err = gauss_cluster_data[key]['energy_err']

    x.append(1./beta)
    y.append(energy_mean)
    #y.append((cluster_data[key]['charges'][100000:]**2/key[0]**2).mean())
    yerr.append(energy_err)
    
plt.errorbar(x,y,yerr, fmt='s', markerfacecolor='none',capsize=1.5)#,label='Gauss cluster')
plt.xlim(0,0.6)
plt.ylim(ymin=0.48)

plt.ylabel(r'$E_{\mathcal P}$')
plt.xlabel(r'$\frac{1}{\beta}$')
plt.suptitle('Energy continuum limit')
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(bottom=0.2)
#plt.legend()

plt.savefig('gfx/cluster_energy_cont.pgf')

