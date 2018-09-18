import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')

import matplotlib.pyplot as plt
from skimage.filters import gaussian

image = plt.imread('data/cappadocia.jpg')

sigmas=[0,3,6,9]

fig, axs = plt.subplots(2,2, figsize=(4.7,3.7))
for ax, sigma in zip(axs.flatten(),sigmas):
    filtered = gaussian(image, sigma,multichannel=True,mode='nearest')
    ax.imshow(filtered)
    ax.set_title(r'$\sigma='+'{}'.format(sigma))
    #ticks = [n*N/4 for n in range(5)]
    ax.set_xticks([0,150,300])
    #ax.set_yticks(ticks)

fig.suptitle('Gaussian blur')
#fig.subplots_adjust(top=0.91)
fig.subplots_adjust(bottom=0.1)
#fig.subplots_adjust(hspace=0.14)
fig.subplots_adjust(wspace=0.25)

fig.savefig('gfx/cappadocia.pgf')

