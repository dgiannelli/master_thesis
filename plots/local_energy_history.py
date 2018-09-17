import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import numpy as np
import pickle

with open('data/local_data.pickle','br') as file:
    local_data = pickle.load(file)

#from matplotlib.ticker import ScalarFormatter
#formatter = ScalarFormatter(useMathText=True)
#formatter.set_scientific(True)
#formatter.set_powerlimits((-1,1))

keys = list(local_data)

fig, axs = plt.subplots(int(len(keys)/2.+0.5),2, figsize=(5,5),sharex=True,sharey=True)
for (ax,key) in zip(axs.flatten(),keys):
    therm = local_data[key]['therm']
    ax.plot(local_data[key]['energies'][therm:])
    ax.set_xticks([0,4e5,8e5])
    ax.set_xticklabels(['$0$',r'$4\times10^5$',r'$8\times10^5$'])
    ax.set_xlabel('Iterations',labelpad=10)
    ax.set_ylabel(r'$E_{\mathcal P}$')
    ax.set_title('$N={},\\ \\beta={}$'.format(key[0],key[1]))
    ax.label_outer()
    #ax.xaxis.set_major_formatter(formatter)
    
fig.subplots_adjust(hspace=0.45)
fig.subplots_adjust(top=0.86)
fig.suptitle('Local algorithm: plaquette energy history')

fig.savefig('gfx/local_energy_history.pgf')

