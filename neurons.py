# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:07:03 2023

@author: Albert
"""

neurons = [
[[1.25, 5.12, 4.21], [3.0, 2.1, 0.91], 5],
[[6.10, 78.1, 9.0], [3.0, 1.72, 1.90], 3],
[[2.0, 17.21, 0.91], [2.0, 2.11, 2.09], 1],
[[4.21, 8.10, 10.0], [1.0, 2.11, 8.09], 2]
]

outputs = []

for neuron in neurons:
    out = 0
    
    inputs = neuron[0]
    weights = neuron[1]
    bias = neuron[2]
    
    for i in range(len(inputs)):
        
        out += inputs[i] * weights[i]
        
        
    out += bias
    
    outputs.append([[round(out, 2)], [], 0])

    
print(outputs)


inputs = [1.25, 5.12, 4.21]
weights = [3.0, 2.1, 0.91]
bias = 3

out = 0
for i in range(len(inputs)):
    
    out += inputs[i] * weights[i]
    
out += bias
