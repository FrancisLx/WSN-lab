import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def length(a, b):
    return(a[0] - b[0])**2 + (a[1]-b[1])**2
def simulate(n):
    X = [] #matrix that store the node's pos info
    for i in range(n):
        x = np.random.random()
        y = np.random.random()
        X.append([x, y])
    return X
def transformed(X, n, r):
    Y = np.zeros((n ,n))
    for i in range(n):
        for j in range(n):
            Y[i][j] = np.where(length(X[i], X[j]) <= r**2, 1, 0)
    return Y
def isConnected(X, n):
    tmp = X
    T = X
    for i in range(n-2):
        T = T + np.dot(X, tmp)
        tmp = np.dot(tmp, X)
    return 0 not in T
def fit(n):
    dot = []
    for r in range(50):
        cnt = 0
        for i in range(1000):
            X = simulate(n)
            Y= transformed(X, n, r*0.02)
            if isConnected(Y, n):
                cnt += 1
        dot.append([r*0.02, cnt / 1000.0])
    return dot

df = pd.DataFrame(fit(10))
tmp = df.iloc[:, [0, 1]].values
plt.plot(tmp[:, 0], tmp[:, 1], color = 'black', linestyle = '-', label = 'n = 10')
df_1 = pd.DataFrame(fit(20))
tmp_1 = df_1.iloc[:, [0, 1]].values
plt.plot(tmp_1[:, 0], tmp_1[:, 1], color = 'blue', linestyle = '-.', label = 'n = 20')
df_2 = pd.DataFrame(fit(50))
tmp_2 = df_2.iloc[:, [0, 1]].values
plt.plot(tmp_2[:, 0], tmp_2[:, 1], color = 'cyan', linestyle = '--', label = 'n = 50')
df_3 = pd.DataFrame(fit(100))
tmp_3 = df_3.iloc[:, [0, 1]].values
plt.plot(tmp_3[:, 0], tmp_3[:, 1], color = 'yellow', linestyle = ':', label = 'n = 100')
plt.legend(loc = 'best')
plt.xlabel('Communication radius')
plt.ylabel('Pr[network is connected]')
plt.show()
