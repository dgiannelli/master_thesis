import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import pickle

with open('data/acc_cont_data.pickle','br') as file:
    acc_cont_data = pickle.load(file)

x = []
y = []
yerr = []

for key in acc_cont_data:
    N, beta = key
    local_acc_mean = acc_cont_data[key]['local_acc_mean']
    local_acc_err = acc_cont_data[key]['local_acc_err']

    x.append(1./beta)
    y.append(local_acc_mean)
    yerr.append(local_acc_err)

plt.errorbar(x,y,yerr, fmt='s', markerfacecolor='none',capsize=1.5)
plt.ylim(ymax=1)
plt.xlim(0,0.6)

plt.ylabel('Acceptance')
plt.xlabel(r'$\frac{1}{\beta}$')
plt.suptitle('Local algorithm: Metropolis acceptance ratio')
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(bottom=0.2)

plt.savefig('gfx/local_acc.pgf')

