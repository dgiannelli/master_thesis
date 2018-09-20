import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import pickle

with open('data/side_data.pickle','br') as file:
    side_data = pickle.load(file)

sides = list(side_data.keys())

gauss_acc_means = []
gauss_acc_errs = []

cluster_acc_means = []
cluster_acc_errs = []

for side in sides:
    gauss_acc_means.append(side_data[side]['gauss_cluster_acc_mean'])
    gauss_acc_errs.append(side_data[side]['gauss_cluster_acc_err'])
    
    cluster_acc_means.append(side_data[side]['cluster_acc_mean'])
    cluster_acc_errs.append(side_data[side]['cluster_acc_err'])
    
plt.errorbar(sides,cluster_acc_means,cluster_acc_errs,fmt='s',markerfacecolor='none',capsize=1.5,label='Reverse')
plt.errorbar(sides,gauss_acc_means,gauss_acc_errs,fmt='D',markerfacecolor='none',capsize=1.5,label='Gauss')

plt.suptitle('Square side dependence: Reverse vs Gauss')
plt.xlabel('Square side')
plt.ylabel('Acceptance')
plt.xticks(sides)

plt.subplots_adjust(left=0.2)

plt.legend()

plt.savefig('gfx/cluster_side_acc.pgf')

