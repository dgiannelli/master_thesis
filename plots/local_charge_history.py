import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import numpy as np
import pickle

with open('data/local_data.pickle','br') as file:
    local_data = pickle.load(file)

keys = list(local_data)

fig, axs = plt.subplots(int(len(keys)/2.+0.5),2, figsize=(5,5),sharex=True,sharey=True)
for (ax,key) in zip(axs.flatten(),keys):
    therm = local_data[key]['therm']
    ax.plot(local_data[key]['charges'][therm:])
    ax.set_xticks([0,4e5,8e5])
    ax.set_xticklabels(['$0$',r'$4\times10^5$',r'$8\times10^5$'])
    ax.set_xlabel('Iterations',labelpad=10)
    ax.set_ylabel(r'$Q$')
    ax.set_title('$N={},\\ \\beta={}$'.format(key[0],key[1]))
    ax.label_outer()
    
fig.subplots_adjust(hspace=0.45)
fig.subplots_adjust(top=0.86)
fig.suptitle('Local algorithm: charge history')

fig.savefig('gfx/local_charge_history.pgf')

