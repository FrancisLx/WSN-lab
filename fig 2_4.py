import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def length(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def simulate(n):
    X = []  # matrix that store the node's pos info
    for i in range(n):
        x = np.random.random()
        y = np.random.random()
        X.append([x, y])
    return X


def transformed(X, n, r):
    Y = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            Y[i][j] = np.where(length(X[i], X[j]) <= r ** 2, 1, 0)
    return Y


def isConnected(X, n):
    tmp = X
    T = X
    for i in range(n - 2):
        T = T + np.dot(X, tmp)
        tmp = np.dot(tmp, X)
    return 0 not in T


def fit(r):
    dot = []
    for n in range(1,21):
        t = n*5
        cnt = 0
        for i in range(1000):
            X = simulate(t)
            Y = transformed(X, t, r)
            if isConnected(Y, t):
                cnt += 1
        dot.append([t, cnt / 1000.0])
    return dot

df = pd.DataFrame(fit(0.05))
tmp = df.iloc[:, [0, 1]].values
plt.plot(tmp[:, 0], tmp[:, 1], color='black', linestyle='-', label='r = 0.05')

df = pd.DataFrame(fit(0.15))
tmp = df.iloc[:, [0, 1]].values
plt.plot(tmp[:, 0], tmp[:, 1], color='green', linestyle='-.', label='r = 0.15')

df = pd.DataFrame(fit(0.25))
tmp = df.iloc[:, [0, 1]].values
plt.plot(tmp[:, 0], tmp[:, 1], color = 'blue', linestyle = '--', label = 'r = 0.25')

df = pd.DataFrame(fit(0.35))
tmp = df.iloc[:, [0, 1]].values
plt.plot(tmp[:, 0], tmp[:, 1], color = 'cyan', linestyle = ':', label = 'r = 0.35')


df = pd.DataFrame(fit(0.45))
tmp = df.iloc[:, [0, 1]].values
plt.plot(tmp[:, 0], tmp[:, 1], color = 'yellow', linestyle = '-', label = 'r = 0.45')


plt.legend(loc='best')
plt.xlabel('Number of nodes')
plt.ylabel('Pr[network is connected]')
plt.show()







