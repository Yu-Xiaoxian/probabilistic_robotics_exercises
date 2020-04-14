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
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt

print("Chapter 3: Guassian Filters")
print("")
print("#############")
print("Exercise 3.1:")

A = np.mat([[1,1],[0,1]])
B = np.mat([[0.5], [1.0]])
R = B*B.T
mu = np.mat([[0], [0]])
u = np.mat([0])
Sigma = np.mat([[0,0],[0,0]])

fig = plt.figure()
ax = fig.add_subplot(111)

for i in range(1, 6):
    mu_t = A*mu + B*u
    Sigma_t = A*Sigma*A.T + R
    mu = mu_t
    Sigma = Sigma_t
    print(mu)
    print(Sigma)
    eigen_value, eigen_vector = np.linalg.eig(Sigma)
    ell1 = Ellipse(xy = (0.0, 0.0), width = eigen_value[1], height = eigen_value[0], angle = np.arctan(eigen_vector[1,0]/eigen_vector[0,0])*180.0/3.1415926, facecolor='yellow', alpha=0.3)
    ax.add_patch(ell1)

plt.axis('scaled')
plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length

plt.show()