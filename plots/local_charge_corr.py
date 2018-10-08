import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import numpy as np
from uncertainties import ufloat
import pickle

with open('data/local_data.pickle','br') as file:
    local_data = pickle.load(file)

Ns = []
betas = []
iters = []
therms = []
x = []
y = []
yerr = []

for key in list(local_data)[:-2]:
    N, beta = key
    Ns.append(N)
    betas.append(beta)
    iters.append(local_data[key]['iters'])
    therms.append(local_data[key]['therm'])
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

def latex_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str

measures = [ufloat(mean,err) for mean,err in zip(y,yerr)]
with open('tables/local_charge_corr.tex','w') as file:
    file.write(r'\begin{tabular}{ccccc} \toprule'+'\n')
    file.write(r'$N$ & $\beta$ & Iters & Therm. & $\tau_Q^\mathrm{int}$'+'\n')
    for N,beta,iter,therm,measure in zip(Ns,betas,iters,therms,measures):
        file.write(r'\\ \midrule'+'\n')
        file.write('${}$'.format(N)+' & '+'${}$'.format(beta)+' & '+'${}$'.format(latex_float(iter))+' & '
                  +'${}$'.format(latex_float(therm))+' & '+'${}$'.format(measure.format('.2ufS')))
    file.write(r'\\ \bottomrule'+'\n')
    file.write(r'\end{tabular}'+'\n')

