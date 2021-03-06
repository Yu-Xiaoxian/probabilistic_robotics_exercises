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
# SOFTWARE.

import numpy as np
import random as rd

print("Chapter 2: Recursive State Estimation")
print("")
print("#############")
print("Exercise 2.1:")
p = [0.01, 0.99]
eta = 1

for i in range(1 , 11):
    p = [p[0]*1, p[1]*1/3]
    eta = 1/(p[0] + p[1])
    p = [p[0]*eta, p[1]*eta]
    print(i, p[0], p[1], eta)

print("")
print("#############")
print("Exercise 2.2:")
cnt_weath = [0,0,0]
weath = ["sunny", "cloudy", "windy"]
cnt = 0
trans = [[0.8, 1.0, 1.0],[0.4, 0.8,1.0],[0.2,0.8,1.0]]

yest = 0
today = 0
while cnt < 10000000:
	tran = trans[yest]
	p = rd.random()
	if p < tran[0]:
		today = 0
	elif p < tran[1]:
		today = 1
	else:
		today = 2
	# print(weath[today])
	cnt_weath[today] = cnt_weath[today] + 1
	cnt = cnt+1
	yest = today

print(float(cnt_weath[0])/cnt, float(cnt_weath[1])/cnt, float(cnt_weath[2])/cnt)

print("")
print("#############")
print("Exercise 2.3: a)")
trans = [[0.8, 0.4, 0.2],[0.2, 0.4, 0.6],[0.0,0.2,0.2]]
obser = [[0.6, 0.3, 0.0],[0.4, 0.7, 0.0],[0.0,0.0,0.1]]

bel = [1.0, 0, 0]
z = [1, 1, 2, 0]

for i in range(0,4):
	bar_bel = [bel[0]*trans[0][0] + bel[1]*trans[0][1] + bel[2]*trans[0][2], bel[0]*trans[1][0] + bel[1]*trans[1][1] + bel[2]*trans[1][2], bel[0]*trans[2][0] + bel[1]*trans[2][1] + bel[2]*trans[2][2]]
	bel = [obser[z[i]][0]*bar_bel[0], obser[z[i]][1]*bar_bel[1], obser[z[i]][2]*bar_bel[2]]
	eta = 1/(bel[0] + bel[1] + bel[2])
	bel = [bel[0]*eta, bel[1]*eta, bel[2]*eta]
	print("Day ", i+2)
	# print(bar_bel)
	print(bel)
	print(eta)

print("b)")
bel = [1.0, 0, 0]
z = [0, 0, 2]
for i in range(0,3):
	bar_bel = [bel[0]*trans[0][0] + bel[1]*trans[0][1] + bel[2]*trans[0][2], bel[0]*trans[1][0] + bel[1]*trans[1][1] + bel[2]*trans[1][2], bel[0]*trans[2][0] + bel[1]*trans[2][1] + bel[2]*trans[2][2]]
	bel = [obser[z[i]][0]*bar_bel[0], obser[z[i]][1]*bar_bel[1], obser[z[i]][2]*bar_bel[2]]
	eta = 1/(bel[0] + bel[1] + bel[2])
	bel = [bel[0]*eta, bel[1]*eta, bel[2]*eta]
	print("Day ", i+2)
	# print(bar_bel)
	print(bel)
	print(eta)
