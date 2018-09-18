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
    sweep_acc_mean = local_data[key]['sweep_acc_mean']
    sweep_acc_err = local_data[key]['sweep_acc_err']

    x.append(1./beta)
    y.append(sweep_acc_mean)
    yerr.append(sweep_acc_err)
    
plt.errorbar(x,y,yerr, fmt='s',markerfacecolor='none',capsize=1.5)
plt.xlim(xmin=0)
plt.ylim(ymax=1.)
plt.ylabel('Acceptance')
plt.xlabel(r'$\frac{1}{\beta}$')
plt.suptitle('Local algorithm: Metropolis acceptance ratio')
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(bottom=0.2)

plt.savefig('gfx/local_acc.pgf')
