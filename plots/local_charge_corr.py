import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import pickle

with open('data/local_data.pickle','br') as file:
    local_data = pickle.load(file)

x = []
y = []
yerr = []

for key in list(local_data)[:-2]:
    N, beta = key
    charge_corr_mean = local_data[key]['charge_corr_mean']
    charge_corr_err = local_data[key]['charge_corr_err']

    x.append(1./beta)
    y.append(charge_corr_mean)
    yerr.append(charge_corr_err)

plt.errorbar(x,y,yerr, fmt='s',markerfacecolor='none',capsize=1.5)
#plt.ylim(ymax=1)
plt.xlim(xmin=0)

plt.ylabel(r'$\tau_Q^\mathrm{int}$')
plt.xlabel(r'$\frac{1}{\beta}$')
plt.suptitle('Local algorithm: charge autocorrelation time')
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(bottom=0.2)

plt.savefig('gfx/local_charge_corr.pgf')

