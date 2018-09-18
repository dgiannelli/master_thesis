import matplotlib as mpl
mpl.use('pgf')
mpl.rcParams['text.latex.preamble']=[r"\usepackage{amssymb}",
                                             r"\usepackage{amsmath}"]
#rc_params = {
#    'font.family': 'serif',  # use serif/main font for text elements
#    'text.usetex': True,    # use inline math for ticks
#    #'text.latex.unicode' : False,
#    'pgf.rcfonts': False,   # don't setup fonts from rc parameters
#    'font.size' : 10,
#    'figure.figsize' : (4, 3),
#    #'figure.subplot.top' : 0.75,
#    #'figure.autolayout' : True,
#    'figure.subplot.left'    : 0.125,
#    'figure.subplot.right'   : 0.9,
#    'figure.subplot.bottom'  : 0.14,#0.11,
#    'figure.subplot.top'     : 0.88,
#    'figure.subplot.wspace' : 0.2,
#    'figure.subplot.hspace'  : 0.2,
#}
#mpl.rcParams.update(rc_params)

import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
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

fig, axs = plt.subplots(1,2,figsize=(4.7,3), sharex=True, sharey=True)
x = np.linspace(-np.pi,np.pi,1000)
for (k, ax) in zip(ks,axs):
    p=P(k)
    g=G(k)
    pdf = ax.plot(x,p(x))
    gaus = ax.plot(x,g(x))

    ax.set_xlabel('$x$')
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
    ax.set_title('$k={}$'.format(k), size='medium')


axs[0].set_ylabel('$p(x)$')
fig.suptitle("Laplace's method")#, y=1.)
fig.legend((pdf[0],gaus[0]), (r'$\propto e^{k\cos x}$',r'$\propto e^{-kx^2/2}$'),
        ncol=2, loc='upper center', bbox_to_anchor=(0.5,0.14))
fig.subplots_adjust(bottom=0.27, top=0.85)
#fig.tight_layout()
#fig.subplots_adjust(wspace=0)
fig.savefig('gfx/gauss.pgf')

