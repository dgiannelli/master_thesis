import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import numpy as np
from uncertainties import ufloat
import pickle

with open('data/acc_cont_data.pickle','br') as file:
    acc_cont_data = pickle.load(file)

Ns = []
betas = []
x = []
reverse_cluster_means = []
reverse_cluster_errs = []
gauss_cluster_means = []
gauss_cluster_errs = []
samples = []
sides = []

for key in acc_cont_data:
    N, beta = key
    Ns.append(N)
    betas.append(beta)
    x.append(1./beta)
    reverse_cluster_means.append(acc_cont_data[key]['reverse_cluster_acc_mean'])
    reverse_cluster_errs.append(acc_cont_data[key]['reverse_cluster_acc_err'])
    gauss_cluster_means.append(acc_cont_data[key]['gauss_cluster_acc_mean'])
    gauss_cluster_errs.append(acc_cont_data[key]['gauss_cluster_acc_err'])
    samples.append(acc_cont_data[key]['sample'])
    sides.append(acc_cont_data[key]['side'])
    
fig, ax = plt.subplots(figsize=(4.7,3))
ax.errorbar(x,reverse_cluster_means,reverse_cluster_errs,fmt='s',markerfacecolor='none',capsize=1.5,label='Reverse')
ax.errorbar(x,gauss_cluster_means,gauss_cluster_errs,fmt='D',markerfacecolor='none',capsize=1.5,label='Gauss')

ax.legend()
ax.set_ylim(ymin=0)
ax.set_xlim(0,0.6)

fig.suptitle('Cluster acceptance continuum limit: Reverse vs Gauss')
ax.set_xlabel(r'$\frac{1}{\beta}$')
ax.set_ylabel('Acceptance')

fig.subplots_adjust(left=0.2)
fig.subplots_adjust(right=0.8)
fig.subplots_adjust(bottom=0.2)

fig.savefig('gfx/cluster_acc_cont.pgf')

def latex_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str

reverse_measures = [ufloat(mean,err) for mean,err in zip(reverse_cluster_means,reverse_cluster_errs)]
gauss_measures = [ufloat(mean,err) for mean,err in zip(gauss_cluster_means,gauss_cluster_errs)]
with open('tables/cluster_acc_cont.tex','w') as file:
    file.write(r'\begin{tabular}{cccccc} \toprule'+'\n')
    file.write(r'$N$ & $\beta$ & Sample & Cluster side & Reverse acc. & Gauss acc.'+'\n')
    for N,beta,sample,side,reverse_measure,gauss_measure in zip(Ns,betas,samples,sides,reverse_measures,gauss_measures):
        file.write(r'\\ \midrule'+'\n')
        file.write('${}$'.format(N)+' & '+'${}$'.format(beta)+' & '+'${}$'.format(latex_float(sample))+' & '
                  +'${}$'.format(side)+' & '+'${:.2ufS}$'.format(reverse_measure)+' & '+'${:.2ufS}$'.format(gauss_measure))
    file.write(r'\\ \bottomrule'+'\n')
    file.write(r'\end{tabular}'+'\n')

