import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import pickle
import numpy as np
from uncertainties import ufloat

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
    susc_mean = gauss_cluster_data[key]['susc_mean']
    susc_err = gauss_cluster_data[key]['susc_err']

    x.append(1./beta)
    y.append(susc_mean)
    yerr.append(susc_err)

fig, axs = plt.subplots(1,2,figsize=(4.7,3),sharey=True)

axs[1].errorbar(x,y,yerr, fmt='s', markerfacecolor='none',capsize=1.5,label='Gauss cluster')
axs[1].set_xlim(xmin=0, xmax=0.6)
axs[1].set_ylim(ymin=0.0225)
axs[1].legend(loc=2)
axs[1].set_xlabel(r'$1/\beta$')
axs[1].tick_params(axis='y',direction='inout')

beta_durr, y_durr, yerr_durr = np.loadtxt('data/durr-hoelbling.dat',unpack=True)
axs[0].errorbar(1/beta_durr,y_durr,yerr_durr, fmt='D',color='C1',markerfacecolor='none',capsize=1.5,label='Durr-Hoelbling')
axs[0].set_xlim(xmin=0.6,xmax=0)
axs[0].legend(loc=1)
axs[0].set_xlabel(r'$1/\beta$')
axs[0].set_ylabel(r'$\chi/g^2$')

ticks = axs[0].xaxis.get_major_ticks()
ticks[0].label1.set_visible(False)

fig.suptitle('Topological susceptivity: continuum limit')
fig.subplots_adjust(wspace=0)
fig.subplots_adjust(left=0.15)
fig.subplots_adjust(right=0.85)
fig.subplots_adjust(bottom=0.15)

plt.savefig('gfx/cluster_susc_cont.pgf')

def latex_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str

measures = [ufloat(mean,err) for mean,err in zip(y,yerr)]
with open('tables/cluster_susc_cont.tex','w') as file:
    file.write(r'\begin{tabular}{ccccccc} \toprule'+'\n')
    file.write(r'$N$ & $\beta$ & Side & Repets & Iters & Therm. & $\chi/g^2$'+'\n')
    for N,beta,side,repet,iter,therm,measure in zip(Ns,betas,sides,repets,iters,therms,measures):
        file.write(r'\\ \midrule'+'\n')
        file.write('${}$'.format(N)+' & '+'${}$'.format(beta)+' & '+'${}$'.format(side)+' & '+'${}$'.format(repet)+' & '
                  +'${}$'.format(latex_float(iter))+' & '+'${}$'.format(latex_float(therm))+' & '+'${}$'.format(measure.format('.2uS')))
    file.write(r'\\ \bottomrule'+'\n')
    file.write(r'\end{tabular}'+'\n')

