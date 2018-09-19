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
    susc_mean = gauss_cluster_data[key]['susc_mean']
    susc_err = gauss_cluster_data[key]['susc_err']

    x.append(1./beta)
    y.append(susc_mean)
    #y.append((cluster_data[key]['charges'][100000:]**2/key[0]**2).mean())
    yerr.append(susc_err)
    
plt.errorbar(x,y,yerr, fmt='s', markerfacecolor='none',capsize=1.5,label='Gauss cluster')
#plt.xlim(xmin=0)
#plt.ylim(ymin=0.022)
#print(y[3], yerr[3]) 

beta_durr, y_durr, yerr_durr = np.loadtxt('data/durr-hoelbling.dat',unpack=True)
plt.errorbar(1/beta_durr,y_durr,yerr_durr, fmt='D',markerfacecolor='none',capsize=1.5,label='Durr-Hoelbling')

plt.ylabel(r'$\frac{\chi}{g^2}$')
plt.xlabel(r'$\frac{1}{\beta}$')
plt.suptitle('Topological susceptivity')
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(bottom=0.2)
plt.legend()

plt.savefig('gfx/susc_cont.pgf')

