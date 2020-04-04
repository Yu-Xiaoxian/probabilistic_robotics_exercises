#    Copyright [2020] [Yu-Xiaoxian and other contributors]

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

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