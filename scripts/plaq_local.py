import pickle
from uncertainties import ufloat

with open('data/local_data.pickle','br') as file:
    local_data = pickle.load(file)

N = 24
beta = 7.2

mean = local_data[(N,beta)]['energy_mean']
err = local_data[(N,beta)]['energy_err']

measure = ufloat(mean,err)

with open('tables/plaq_local.tex','w') as file:
    file.write(measure.format('.2uS'))

