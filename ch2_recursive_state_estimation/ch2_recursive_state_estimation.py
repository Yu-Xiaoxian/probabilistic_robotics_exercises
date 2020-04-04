import numpy as np

print("Chapter 2: Recursive State Estimation")
print("Exercise 1:")
p = [0.01, 0.99]
eta = 1

for i in range(1 , 11):
    p = [p[0]*1, p[1]*1/3]
    eta = 1/(p[0] + p[1])
    p = [p[0]*eta, p[1]*eta]
    print(i, p[0], p[1], eta)