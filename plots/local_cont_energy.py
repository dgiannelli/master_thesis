import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import numpy as np
import pickle

with open('data/local_data.pickle','br') as file:
    local_data = pickle.load(file)

x = []
y = []
yerr = []

for key in local_data:
    N, beta = key
    energy_mean = local_data[key]['energy_mean']
    energy_err = local_data[key]['energy_err']

    x.append(1./beta)
    y.append(energy_mean)
    yerr.append(energy_err)
    
plt.errorbar(x,y,yerr, fmt='s',markerfacecolor='none',capsize=1.5)
plt.xlim(xmin=0)
plt.ylim([0.45,0.625])
plt.ylabel(r'$E_{\mathcal P}$')
plt.xlabel(r'$\frac{1}{\beta}$')
plt.suptitle('Local algorithm: biased energy continuum limit')
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(bottom=0.2)

plt.savefig('gfx/local_cont_energy.pgf')
#plt.savefig('gfx/local_cont_energy.pdf')

