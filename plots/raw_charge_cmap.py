import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import numpy as np
import pickle
import matplotlib.colors as mcols

with open('data/cluster_inv.pickle','br') as file:
    dic = pickle.load(file)

N = dic['N']
beta = dic['beta']
charge_matrix = dic['charge_matrices'][0]
charge = dic['charges'][0]

minimum = 1/N**2
maximum = 100/N**2
norm = mcols.SymLogNorm(linthresh=minimum,
                        linscale=0,
                        vmin=-maximum,
                        vmax=maximum)

xshift=17
yshift=23

fig, ax = plt.subplots(figsize=(3.5,3))
rolled = np.roll(charge_matrix,(yshift,xshift),axis=(0,1))
mesh = ax.pcolormesh(rolled, cmap='RdBu', norm=norm)
ax.set_aspect('equal')
ticks = [n*N/4 for n in range(5)]
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_title('$N = {},\\ \\beta={},\\ Q ={:.0f}$'.format(N,beta,charge_matrix.sum()+0.01),pad=5)

fig.subplots_adjust(top=0.8)
fig.subplots_adjust(bottom=0.1)
fig.subplots_adjust(right=0.75)
#fig.subplots_adjust(hspace=0.14)

cax = fig.add_axes([0.775, 0.1, 0.03, 0.7])
bar = fig.colorbar(mesh, cax=cax, extend='both', orientation='vertical')
bar.set_ticks([-maximum,-10*minimum,0,10*minimum,maximum])
bar.set_ticklabels([r'$-\frac{100}{N^2}$',r'$-\frac{10}{N^2}$',r'$\pm\frac{1}{N^2}$',r'$\frac{10}{N^2}$',r'$\frac{100}{N^2}$'])
bar.set_label(r'$q$')

fig.suptitle('Local charge colormap')
fig.savefig('gfx/raw_charge_cmap.pgf')

