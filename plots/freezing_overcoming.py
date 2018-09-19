import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import pickle

with open('data/local_data.pickle','br') as file:
    local_data = pickle.load(file)

with open('data/gauss_cluster_data.pickle','br') as file:
    gauss_cluster_data = pickle.load(file)

#therm = 

N = 32
beta = 12.8

plt.plot(gauss_cluster_data[(N,beta)]['charges'],label='Cluster algorithm')
plt.plot(local_data[(N,beta)]['charges'],label='Local algorithm')

plt.xlabel('Iterations')
plt.ylabel(r'$Q_\mathrm{tot}$')
plt.title('Charge history')
plt.legend()

plt.subplots_adjust(left=0.15)

plt.savefig('freezing_overcoming.pgf')

