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

def formOutput(neurons):
        
    out = 0
    for neuron in neurons:
        
        inputs = neuron[0]
        weights = neuron[1]
        bias = neuron[2]
        
        for i in range(len(inputs)):
            
            out += inputs[i] * weights[i]
            
        out += bias
        
        return round(out, 2)


hidden_neurons = [
[[3.0, 2.0, 1.5, 2.5],   [0.8, 0.3, 0.2, 0.4],    3],
[[2.0, 3.0, 1.25, 2.25], [0.3, 0.8, 0.15, 0.35],  4],
[[3.0, 2.0, 1.25, 2.0],  [0.8, 0.3, 0.15, 9.3],   6],
[[1.0, 0.5, 0.25, 1.0],  [0.1, 0.01, 0.001, 0.1], 3]    
]

last_neuron = formOutput(hidden_neurons)

print(last_neuron)

def mulitplyInputsWeights(inp, w, b):
    
    n = 0
    
    for i in range(len(inp)):
        n += inp[i] * w[i]
        
    n += b
    
    return b


inp = [1.0, 3.0, 2.0, 1.5]
w1 =  [0.2, 0.8, -0.9, 2.0]
w2 =  [1.0, 2.0, -1.0, 3.0]
w3 =  [2.0, 1.9, 2.7, 3.5]

bias1, bias2, bias3 = 2, 3, 0.5

n_out = [
    mulitplyInputsWeights(inp, w1, bias1),
    mulitplyInputsWeights(inp, w2, bias2),
    mulitplyInputsWeights(inp, w3, bias3)
    ]

print(n_out)