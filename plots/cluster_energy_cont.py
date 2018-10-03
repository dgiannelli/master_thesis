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
    energy_mean = gauss_cluster_data[key]['energy_mean']
    energy_err = gauss_cluster_data[key]['energy_err']

    x.append(1./beta)
    y.append(energy_mean)
    #y.append((cluster_data[key]['charges'][100000:]**2/key[0]**2).mean())
    yerr.append(energy_err)
    
fig, ax = plt.subplots(figsize=(4.7,3))
ax.errorbar(x,y,yerr, fmt='s', markerfacecolor='none',capsize=1.5)#,label='Gauss cluster')
ax.set_xlim(0,0.6)
ax.set_ylim(ymin=0.48)
ax.set_ylabel(r'$E[\mathcal P]$')
ax.set_xlabel(r'$1/\beta$')
fig.suptitle('Energy continuum limit')
fig.subplots_adjust(left=0.20)
fig.subplots_adjust(right=0.80)
fig.subplots_adjust(bottom=0.15)
#plt.legend()

plt.savefig('gfx/cluster_energy_cont.pgf')

def latex_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str

measures = [ufloat(mean,err) for mean,err in zip(y,yerr)]
with open('tables/cluster_energy_cont.tex','w') as file:
    file.write(r'\begin{tabular}{ccccccc} \toprule'+'\n')
    file.write(r'$N$ & $\beta$ & Side & Repeats & Iters & Therm. & $E[\mathcal P]$'+'\n')
    for N,beta,side,repet,iter,therm,measure in zip(Ns,betas,sides,repets,iters,therms,measures):
        file.write(r'\\ \midrule'+'\n')
        file.write('${}$'.format(N)+' & '+'${}$'.format(beta)+' & '+'${}$'.format(side)+' & '+'${}$'.format(repet)+' & '
                  +'${}$'.format(latex_float(iter))+' & '+'${}$'.format(latex_float(therm))+' & '+'${}$'.format(measure.format('.2uS')))
    file.write(r'\\ \bottomrule'+'\n')
    file.write(r'\end{tabular}'+'\n')

