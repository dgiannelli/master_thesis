import pickle


with open('data/local_data.pickle','br') as file:
    local_data = pickle.load(file)

Ns = []
betas = []
iters = []
therms = []

for N, beta in local_data:
    Ns.append(N)
    betas.append(beta)
    iters.append(len(local_data[(N,beta)]['energies']))
    therms.append(local_data[(N,beta)]['therm'])

size = len(Ns)

def latex_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str

with open('tables/local_cont.tex','w') as file:
    file.write(r'\begin{tabular}{cccc} \toprule'+'\n')
    file.write(r'$N$ & $\beta$ & Iterations & Thermalization'+'\n')
    for N,beta,iter,therm in zip(Ns,betas,iters,therms):
        file.write(r'\\ \midrule'+'\n')
        file.write('${}$'.format(N)+' & '+'${}$'.format(beta)+' & '+'${}$'.format(latex_float(iter))+' & '+'${}$'.format(latex_float(therm)))
    file.write(r'\\ \bottomrule'+'\n')
    file.write(r'\end{tabular}'+'\n')


#with open('tables/local_cont.tex','w') as file:
#    file.write(r'\begin{tabular}{'+'c'+size*'c'+r'} \toprule'+'\n')
#    file.write('$N$ & ' + ' & '.join(['${}$'.format(N) for N in Ns]))
#    file.write(r'\\ \midrule'+'\n')
#    file.write(r'$\beta$ & ' + ' & '.join(['${}$'.format(beta) for beta in betas]))
#    file.write(r'\\ \midrule'+'\n')
#    file.write(r'Iterations & ' + ' & '.join(['${}$'.format(latex_float(iter)) for iter in iters]))
#    file.write(r'\\ \midrule'+'\n')
#    file.write(r'Therm. & ' + ' & '.join(['${}$'.format(latex_float(therm)) for therm in therms]))
#    file.write(r'\\ \bottomrule'+'\n')
#    file.write(r'\end{tabular}'+'\n')

