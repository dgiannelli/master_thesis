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

for key in list(local_data)[:-2]:
    N, beta = key
    susc_mean = local_data[key]['susc_mean']
    susc_err = local_data[key]['susc_err']

    x.append(1./beta)
    y.append(susc_mean)
    yerr.append(susc_err)
    
plt.errorbar(x,y,yerr, fmt='s',markerfacecolor='none',capsize=1.5)
plt.xlim(xmin=0)
#plt.ylim([0.45,0.625])
plt.ylabel(r'$\frac{\chi}{g^2}$')
plt.xlabel(r'$\frac{1}{\beta}$')
plt.suptitle(r'Local algorithm: biased $\chi/g^2$ continuum limit')
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(bottom=0.2)

plt.savefig('gfx/local_cont_susc.pgf')

