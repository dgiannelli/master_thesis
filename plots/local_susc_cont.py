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

for key in list(local_data)[:-1]:
    N, beta = key
    Ns.append(N)
    betas.append(beta)
    iters.append(local_data[key]['iters'])
    therms.append(local_data[key]['therm'])
    susc_mean = local_data[key]['susc_mean']
    susc_err = local_data[key]['susc_err']

    x.append(1./beta)
    y.append(susc_mean)
    yerr.append(susc_err)
    
plt.errorbar(x,y,yerr, fmt='s',markerfacecolor='none',capsize=1.5)
plt.xlim(xmin=0)
#plt.ylim([0.45,0.625])
plt.ylabel(r'$\frac{\chi}{g^2}$')
plt.xlabel(r'$1/\beta$')
plt.suptitle(r'Local algorithm: biased $\chi/g^2$ continuum limit')
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(right=0.8)
plt.subplots_adjust(bottom=0.15)

plt.savefig('gfx/local_susc_cont.pgf')

def latex_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str

measures = [ufloat(mean,err) for mean,err in zip(y,yerr)]
with open('tables/local_susc_cont.tex','w') as file:
    file.write(r'\begin{tabular}{ccccc} \toprule'+'\n')
    file.write(r'$N$ & $\beta$ & Iters & Therm. & $\chi/g^2$'+'\n')
    for N,beta,iter,therm,measure in zip(Ns,betas,iters,therms,measures):
        file.write(r'\\ \midrule'+'\n')
        file.write('${}$'.format(N)+' & '+'${}$'.format(beta)+' & '+'${}$'.format(latex_float(iter))+' & '
                  +'${}$'.format(latex_float(therm))+' & '+'${}$'.format(measure.format('.2uSL')))
    file.write(r'\\ \bottomrule'+'\n')
    file.write(r'\end{tabular}'+'\n')

