import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import numpy as np
from uncertainties import ufloat
import pickle

with open('data/gauss_cluster_data.pickle','br') as file:
    gauss_cluster_data = pickle.load(file)

Ns = []
betas = []
sides = []
repets = []
iters = []
therms = []
x = []
y = []
yerr = []

for key in list(gauss_cluster_data):
    N, beta = key
    Ns.append(N)
    betas.append(beta)
    sides.append(gauss_cluster_data[key]['side'])
    repets.append(gauss_cluster_data[key]['cluster_repets'])
    iters.append(gauss_cluster_data[key]['iters'])
    therms.append(gauss_cluster_data[key]['therm'])
    charge_corr_mean = gauss_cluster_data[key]['charge_corr_mean']
    charge_corr_err = gauss_cluster_data[key]['charge_corr_err']

    x.append(1./beta)
    y.append(charge_corr_mean)
    yerr.append(charge_corr_err)

plt.errorbar(x,y,yerr, fmt='s',markerfacecolor='none',capsize=1.5)
#plt.ylim(ymax=1)
plt.xlim(xmin=0)

plt.ylabel(r'$\tau_Q^\mathrm{int}$')
plt.xlabel(r'$1/\beta$')
plt.suptitle('Gauss cluster algorithm: charge autocorrelation time')
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(right=0.8)
plt.subplots_adjust(bottom=0.15)

plt.savefig('gfx/cluster_charge_corr.pgf')

def latex_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str

measures = [ufloat(mean,err) for mean,err in zip(y,yerr)]
with open('tables/cluster_charge_corr.tex','w') as file:
    file.write(r'\begin{tabular}{ccccccc} \toprule'+'\n')
    file.write(r'$N$ & $\beta$ & Side & Repeats & Iters & Therm. & $\tau_Q^\mathrm{int}$'+'\n')
    for N,beta,side,repet,iter,therm,measure in zip(Ns,betas,sides,repets,iters,therms,measures):
        file.write(r'\\ \midrule'+'\n')
        file.write('${}$'.format(N)+' & '+'${}$'.format(beta)+' & '+'${}$'.format(side)+' & '+'${}$'.format(repet)+' & '
                  +'${}$'.format(latex_float(iter))+' & '+'${}$'.format(latex_float(therm))+' & '+'${}$'.format(measure.format('.2uS')))
    file.write(r'\\ \bottomrule'+'\n')
    file.write(r'\end{tabular}'+'\n')

