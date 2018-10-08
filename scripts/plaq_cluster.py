import pickle
from uncertainties import ufloat

with open('data/gauss_cluster_data.pickle','br') as file:
    local_data = pickle.load(file)

N = 24
beta = 7.2

mean = local_data[(N,beta)]['energy_mean']
err = local_data[(N,beta)]['energy_err']

measure = ufloat(mean,err)

with open('tables/plaq_cluster.tex','w') as file:
    file.write(measure.format('.2uS'))

