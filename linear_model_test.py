import matplotlib.pyplot as plt
from sklearn import linear_model as sk_lm 
import numpy as np

import linear_model as cb_lm

def run():
    np.random.seed(16)
    X = np.arange(10,150,2, dtype="float64")
    X += np.random.randn(X.shape[0])
    X = X.reshape(X.shape[0],1)
    y = 2.5 * np.arange(10,150,2, dtype="float64") - 24
    y += np.random.randn(y.shape[0])
    y = y.reshape(y.shape[0],1)

    scores = [cb_lm.LinearRegression(num_iterations=100, learning_rate=lr/100000).fit(X,y).costs_ for lr in range(100)]
    plt.style.use('seaborn-darkgrid')
    palette = plt.get_cmap('hsv')
    for idx, lr in enumerate(range(1,10)):
        plt.plot(scores[lr][20:], color=palette(10*idx), linewidth=1, alpha=0.9, label=f"learning_rate {lr/100000}")
    plt.xlabel("Number of iterations")
    plt.ylabel("Cost")
    plt.title("Gradient descent with different learning rates")
    plt.legend()
    plt.show()