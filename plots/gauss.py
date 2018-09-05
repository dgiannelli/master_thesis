import matplotlib as mpl
mpl.use('pgf')
rc_params = {
    'font.family': 'serif',  # use serif/main font for text elements
    'text.usetex': True,    # use inline math for ticks
    #'text.latex.unicode' : False,
    'pgf.rcfonts': False,   # don't setup fonts from rc parameters
    'font.size' : 10,
    'figure.figsize' : (4, 3),
    #'figure.subplot.top' : 0.75,
    #'figure.autolayout' : True,
    'figure.subplot.left'    : 0.125,
    'figure.subplot.right'   : 0.9,
    'figure.subplot.bottom'  : 0.14,#0.11,
    'figure.subplot.top'     : 0.88,
    'figure.subplot.wspace' : 0.2,
    'figure.subplot.hspace'  : 0.2,
}
mpl.rcParams.update(rc_params)

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

class P:
    def __init__(self, k):
        #self.k = k
        self.fun = lambda x: np.exp(k*np.cos(x))
        self.norm = quad(self.fun, -np.pi, np.pi)[0]
    def __call__(self, x):
        return self.fun(x)/self.norm

class G:
    def __init__(self, k):
        #self.k = k
        self.fun = lambda x: np.exp(-k*x**2/2)
        self.norm = quad(self.fun, -np.pi, np.pi)[0]
    def __call__(self, x):
        return self.fun(x)/self.norm

ks = [1, 3]

fig, axs = plt.subplots(1,2,figsize=(5,3), sharex=True, sharey=True)
x = np.linspace(-np.pi,np.pi,1000)
for (k, ax) in zip(ks,axs):
    p=P(k)
    g=G(k)
    pdf = ax.plot(x,p(x))
    gaus = ax.plot(x,g(x))

    ax.set_xlabel('xlabel')
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
    ax.set_title('$k={}$'.format(k), size='medium')


axs[0].set_ylabel('ylabel')
fig.suptitle("Laplace's method")
fig.legend((pdf[0],gaus[0]), (r'$\sim e^{k\cos x}$',r'$\sim e^{-kx^2/2}$'),
        ncol=2, loc='upper center', bbox_to_anchor=(0.5,0.11))
fig.subplots_adjust(bottom=0.28)
#fig.tight_layout()
#fig.subplots_adjust(wspace=0)
fig.savefig('gauss.pgf')

