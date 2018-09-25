import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import pickle

with open('data/side_data.pickle','br') as file:
    side_data = pickle.load(file)

sides = list(side_data.keys())

Ns = []
betas = []
samples = []
gauss_cluster_acc_means = []
gauss_cluster_acc_errs = []
reverse_cluster_acc_means = []
reverse_cluster_acc_errs = []

for side in sides:
    Ns.append(side_data[side]['N'])
    betas.append(side_data[side]['beta'])
    samples.append(side_data[side]['sample'])
    gauss_cluster_acc_means.append(side_data[side]['gauss_cluster_acc_mean'])
    gauss_cluster_acc_errs.append(side_data[side]['gauss_cluster_acc_err'])
    reverse_cluster_acc_means.append(side_data[side]['reverse_cluster_acc_mean'])
    reverse_cluster_acc_errs.append(side_data[side]['reverse_cluster_acc_err'])
    
fig, ax = plt.subplots(figsize=(4.7,3))
ax.errorbar(sides,reverse_cluster_acc_means,reverse_cluster_acc_errs,fmt='s',markerfacecolor='none',capsize=1.5,label='Reverse')
ax.errorbar(sides,gauss_cluster_acc_means,gauss_cluster_acc_errs,fmt='D',markerfacecolor='none',capsize=1.5,label='Gauss')

fig.suptitle('Square side dependence: Reverse vs Gauss')
ax.set_xlabel('Square side')
ax.set_ylabel('Acceptance')
ax.set_xticks(sides)

fig.subplots_adjust(left=0.2)
fig.subplots_adjust(right=0.8)

ax.legend()

fig.savefig('gfx/cluster_acc_side.pgf')

def latex_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str

with open('tables/cluster_acc_side.tex','w') as file:
    file.write(r'\begin{tabular}{cccc} \toprule'+'\n')
    file.write(r'$N$ & $\beta$ & Sample & Square side'+'\n')
    for N,beta,sample,side in zip(Ns,betas,samples,sides):
        file.write(r'\\ \midrule'+'\n')
        file.write('${}$'.format(N)+' & '+'${}$'.format(beta)+' & '+'${}$'.format(latex_float(sample))+' & '+'${}$'.format(side))
    file.write(r'\\ \bottomrule'+'\n')
    file.write(r'\end{tabular}'+'\n')

