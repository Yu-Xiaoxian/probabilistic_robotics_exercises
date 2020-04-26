# MIT License

# Copyright (c) [2020] [Yu-Xiaoxian and other contributors]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print("Chapter 4: Nonparametric Filters")
print("")
print("#############")
print("Exercise 4.1:")

A=np.mat([[1, 1], [0, 1]])
B=np.mat([[0.5], [1.0]])
mu=np.mat([[0], [0]])
R=B*B.T
Sigma=np.mat([[2.5, 2.0], [2.0, 2.0]])

fig=plt.figure()

ax = fig.add_subplot(1,1,1, projection='3d')
X=np.arange(-10, 10, 1.10)
X_dot=np.arange(-10, 10, 1.10)
X, X_dot=np.meshgrid(X, X_dot)
P_bar=np.zeros(X.shape)

# calculate probabilitics
for i in range(P_bar.shape[0]):
    for j in range(P_bar.shape[1]):
        X_temp=np.mat([[X[i][j]], [X_dot[i][j]]])
        P_bar[i][j]=math.pow(math.e, -1.0/2.0 * X_temp.T * Sigma.I * X_temp)

ax.plot_surface(X, X_dot, P_bar, rstride=1, cstride=1, cmap='rainbow')

plt.show()
