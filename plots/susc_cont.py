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

fig, axs = plt.subplots(1,2,figsize=(4.7,3),sharey=True)

axs[1].errorbar(x,y,yerr, fmt='s', markerfacecolor='none',capsize=1.5,label='Gauss cluster')
axs[1].set_xlim(xmin=0, xmax=0.6)
axs[1].set_ylim(ymin=0.0225)
axs[1].legend()
axs[1].set_xlabel(r'$\frac{1}{\beta}$')
axs[1].tick_params(axis='y',direction='inout')

beta_durr, y_durr, yerr_durr = np.loadtxt('data/durr-hoelbling.dat',unpack=True)
axs[0].errorbar(1/beta_durr,y_durr,yerr_durr, fmt='D',color='C1',markerfacecolor='none',capsize=1.5,label='Durr-Hoelbling')
axs[0].set_xlim(xmin=0.6,xmax=0)
axs[0].legend()
axs[0].set_xlabel(r'$\frac{1}{\beta}$')
axs[0].set_ylabel(r'$\frac{\chi}{g^2}$')

ticks = axs[0].xaxis.get_major_ticks()
ticks[0].label1.set_visible(False)

fig.suptitle('Topological susceptivity: continuum limit')
fig.subplots_adjust(wspace=0)
fig.subplots_adjust(left=0.221)
fig.subplots_adjust(right=0.983)
fig.subplots_adjust(bottom=0.20)

plt.savefig('gfx/susc_cont.pgf')

