import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import numpy as np
import pickle
from scipy.ndimage import gaussian_filter
import matplotlib.colors as mcols
from matplotlib.patches import Rectangle

with open('data/cluster_inv.pickle','br') as file:
    dic = pickle.load(file)

N = dic['N']
beta = dic['beta']
charge_matrices = dic['charge_matrices'][-2:]
charges = dic['charges'][-2:]

minimum = 1/N**2
maximum = 100/N**2
norm = mcols.SymLogNorm(linthresh=minimum,
                        linscale=0,
                        vmin=-maximum,
                        vmax=maximum)

sigma=2.
xshift=17
yshift=23

fig, axs = plt.subplots(1,2, figsize=(5,3.55))
for ax, charge_matrix, charge in zip(axs.flatten(),charge_matrices,charges):
    filtered = gaussian_filter(charge_matrix, sigma, mode='wrap')
    rolled = np.roll(filtered,(yshift,xshift),axis=(0,1))
    mesh = ax.pcolormesh(rolled, cmap='RdBu', norm=norm)
    ax.set_aspect('equal')
    ax.set_title(r'$Q_\mathrm{tot} ='+'{:.0f}$'.format(charge+0.1))
    ticks = [n*N/4 for n in range(5)]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.add_patch(Rectangle((11,12),16,16,facecolor='none',edgecolor='black',lw=0.5))

fig.subplots_adjust(top=0.93)
fig.subplots_adjust(bottom=0.23)
#fig.subplots_adjust(hspace=0.14)
cax = fig.add_axes([0.15,0.15,0.7,0.035])
bar = fig.colorbar(mesh, cax=cax, extend='both', orientation='horizontal')
bar.set_ticks([-maximum,-10*minimum,0,10*minimum,maximum])
bar.set_ticklabels([r'$-\frac{100}{N^2}$',r'$-\frac{10}{N^2}$',r'$\pm\frac{1}{N^2}$',r'$\frac{10}{N^2}$',r'$\frac{100}{N^2}$'])
bar.ax.set_title(r'$Q_\mathrm{loc}$')
fig.suptitle('Cluster update: $N={},\\ \\beta={},\\ \\sigma={}$'.format(N,beta,sigma))

fig.savefig('gfx/cluster_inv.pgf')

