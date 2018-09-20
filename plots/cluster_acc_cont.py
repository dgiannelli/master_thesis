import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import pickle

with open('data/acc_cont_data.pickle','br') as file:
    acc_cont_data = pickle.load(file)

x = []

cluster_means = []
cluster_errs = []

gauss_cluster_means = []
gauss_cluster_errs = []

for key in acc_cont_data:
    N, beta = key
    cluster_acc_mean = acc_cont_data[key]['cluster_acc_mean']
    cluster_acc_err = acc_cont_data[key]['cluster_acc_err']
    
    gauss_cluster_acc_mean = acc_cont_data[key]['gauss_cluster_acc_mean']
    gauss_cluster_acc_err = acc_cont_data[key]['gauss_cluster_acc_err']

    x.append(1./beta)

    cluster_means.append(acc_cont_data[key]['cluster_acc_mean'])
    cluster_errs.append(acc_cont_data[key]['cluster_acc_err'])
    
    gauss_cluster_means.append(acc_cont_data[key]['gauss_cluster_acc_mean'])
    gauss_cluster_errs.append(acc_cont_data[key]['gauss_cluster_acc_err'])
    
    
plt.errorbar(x,cluster_means,cluster_errs,fmt='s',markerfacecolor='none',capsize=1.5,label='Reverse')
plt.errorbar(x,gauss_cluster_means,gauss_cluster_errs,fmt='D',markerfacecolor='none',capsize=1.5,label='Gauss')

plt.legend()
plt.ylim(ymin=0)
plt.xlim(0,0.6)

plt.suptitle('Cluster acceptance continuum limit: Reverse vs Gauss')
plt.xlabel(r'$\frac{1}{\beta}$')
plt.ylabel('Acceptance')

plt.subplots_adjust(left=0.2)
plt.subplots_adjust(bottom=0.2)

plt.savefig('gfx/cluster_acc_cont.pgf')

