import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import numpy as np
import pickle
from scipy.ndimage import gaussian_filter
import matplotlib.colors as mcols

with open('data/cluster_inv.pickle','br') as file:
    dic = pickle.load(file)

N = dic['N']
beta = dic['beta']
charge_matrix = dic['charge_matrices'][0]
#charge = dic['charges'][0]

minimum = 1/N**2
maximum = 100/N**2
norm = mcols.SymLogNorm(linthresh=minimum,
                        linscale=0,
                        vmin=-maximum,
                        vmax=maximum)

xshift=17
yshift=23
sigmas=[0.,1.,1.5,2.]

fig, axs = plt.subplots(2,2, figsize=(4.7,6))
for ax, sigma in zip(axs.flatten(),sigmas):
    filtered = gaussian_filter(charge_matrix, sigma, mode='wrap')
    rolled = np.roll(filtered,(yshift,xshift),axis=(0,1))
    mesh = ax.pcolormesh(rolled, cmap='RdBu', norm=norm)
    ax.set_aspect('equal')
    ax.set_title(r'$\sigma=' + '{}'.format(sigma) + r',\ Q_\mathrm{tot} ='+'{:.0f}$'.format(charge_matrix.sum()+0.01))
    ticks = [n*N/4 for n in range(5)]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)

fig.subplots_adjust(top=0.91)
fig.subplots_adjust(bottom=0.19)
fig.subplots_adjust(hspace=0.14)
cax = fig.add_axes([0.15,0.1,0.7,0.02])
bar = fig.colorbar(mesh, cax=cax, extend='both', orientation='horizontal')
bar.set_ticks([-maximum,-10*minimum,0,10*minimum,maximum])
bar.set_ticklabels([r'$-\frac{100}{N^2}$',r'$-\frac{10}{N^2}$',r'$\pm\frac{1}{N^2}$',r'$\frac{10}{N^2}$',r'$\frac{100}{N^2}$'])
bar.ax.set_title(r'$Q_\mathrm{loc}$')
fig.suptitle('Charge Gaussian blur: $N={},\\ \\beta={}$'.format(N,beta))

fig.savefig('gfx/charge_blur.pgf')

