import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.style.use('./plots/a4.mplstyle')
import pickle

with open('data/local_data.pickle','br') as file:
    local_data = pickle.load(file)

with open('data/gauss_cluster_data.pickle','br') as file:
    gauss_cluster_data = pickle.load(file)


N = 32
beta = 12.8

therm = local_data[(N,beta)]['therm']

plt.plot(gauss_cluster_data[(N,beta)]['charges'][therm:],label='Cluster algorithm')
plt.plot(local_data[(N,beta)]['charges'][therm:]+4,label='Local algorithm')

plt.xlabel('Iterations')
plt.ylabel('$Q$')
plt.title('Charge history: $N={},\ \\beta={}$'.format(N,beta))
plt.legend(loc=1)
plt.xticks([0,4e5,8e5],['$0$',r'$4\times10^5$',r'$8\times10^5$'])
plt.ylim(-10,10)
#plt.yticks(range(-10,11))

plt.subplots_adjust(left=0.15)

plt.savefig('gfx/freezing_overcoming.pgf')

