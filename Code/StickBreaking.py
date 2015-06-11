import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#sticking processing to build a Dirichlet Distribution 
def stick_breaking(alpha,k):
    betas = np.random.beta(1,alpha,k)
    remaining = np.append(1,np.cumprod(1-betas[:-1]))
    p=betas*remaining
    return p/p.sum()

k = 25
alpha = 7
#take k values from the baseline distribution N(0,1)
theta = np.random.normal(0,1,k)
#take the probability value of these points
p = stick_breaking(alpha,k)

#plt.bar(np.arange(k),np.sort(p)[::-1])
#run a experiment 
x = np.random.multinomial(k,p)
#print x
dp = theta[x]
result_x=set(dp)
f= [(dp==i).sum() for i in result_x]
plt.figure
plt.bar(result_x,f,width=.01)
plt.show()


