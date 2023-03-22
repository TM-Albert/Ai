# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:32:00 2023

@author: Albert
"""

import numpy as np

i = [1, 2, 3, 2.5]
w = [0.2, 0.8, -0.5, 1.0]
b = 2

o = np.dot(w, i) + b

inputs = [3, 2.1, 7.9]

weights = [
[1.25, 5.12, 4.21],
[6.10, 78.1, 9.0],
[2.0, 17.21, 0.91]
]

biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases

print(output)
