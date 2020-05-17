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
C = np.mat([1, 0])
Q = 10
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
    ell1 = Ellipse(xy = (mu[0,0], mu[1,0]), width = eigen_value[1], height = eigen_value[0], angle = np.arctan(-eigen_vector[0,0]/eigen_vector[1,0])*180.0/3.1415926, facecolor='yellow', alpha=0.3)
    ax.add_patch(ell1)

print("#############")
print("Exercise 3.2:")

z = np.mat([5])
K = Sigma*C.T*(C*Sigma*C.T+Q).I
mu_5 = mu + K*(z - C*mu)
Sigma_5 = (np.mat(np.identity(2))-K*C)*Sigma
print("K_5: ")
print(K)
print("mu: ")
print(mu_5)
print("Sigma: ")
print(Sigma_5)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.add_patch(ell1)
eigen_value, eigen_vector = np.linalg.eig(Sigma_5)
ell1 = Ellipse(xy = (mu_5[0,0], mu_5[1,0]), width = eigen_value[1], height = eigen_value[0], angle = np.arctan(-eigen_vector[0,0]/eigen_vector[1,0])*180.0/3.1415926, facecolor='blue', alpha=0.3)
ax2.add_patch(ell1)

# plt.axis('scaled')
# plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length

print("#############")
print("Exercise 4.1:")
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
theta = np.linspace(0, 2*np.pi,800)
x,y = np.cos(theta)*1.01, np.sin(theta)*1.01
ax3.plot(x, y, color='blue', linewidth=2.0)

x,y = np.cos(theta)*0.99, np.sin(theta)*0.99
ax3.plot(x, y, color='blue', linewidth=2.0)

v = np.linspace(0.99,1.01,10)
v.shape = (10, 1)
x1 = v * x
y1 = v * y
ax3.plot(x1, y1, color='blue', linewidth=1.0)

print("#############")
print("Exercise 4.3:")
G = np.mat([[1,0,0],[0,1,1],[0,0,1]])
Sigma = np.mat([[0.01,0,0],[0,0.01,0],[0,0,10000]])
Sigma_p = G*Sigma*G.T
print(Sigma_p)

print("#############")
print("Exercise 4.4:")
mu = np.mat([[1],[0],[0]])
z = np.mat([1])
C = np.mat([1,0,0])
Q = np.mat([0.01])
K = Sigma_p*C.T*(C*Sigma_p*C.T+Q).I
mu_f = mu + K*(z - C*mu)
Sigma_f = (np.mat(np.identity(3))-K*C)*Sigma_p
print(K)
print(mu_f)
print(Sigma_f)

print("#############")
print("Exercise 4.5:")
G = np.mat([[1,0,0],[0,1,1],[0,0,1]])
Sigma = np.mat([[0.01,0,0],[0,10000,0],[0,0,0.01]])
Sigma_p = G*Sigma*G.T
print(Sigma_p)
mu = np.mat([[1],[0],[0]])
z = np.mat([1])
C = np.mat([1,0,0])
Q = np.mat([0.01])
K = Sigma_p*C.T*(C*Sigma_p*C.T+Q).I
mu_f = mu + K*(z - C*mu)
Sigma_f = (np.mat(np.identity(3))-K*C)*Sigma_p
print(K)
print(mu_f)
print(Sigma_f)

plt.show()
