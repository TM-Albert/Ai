# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 00:55:24 2023

@author: Albert
"""

import random

class Training:
    
    def __init__(self, inputs, wanted_output):
        self.inputs = inputs
        self.wanted_output = wanted_output
        
    def train(self):
        
        iteration = 0
        output = 0
        while output != self.wanted_output:
            
            output = 0
            searched_weights = [] 
            searched_weight = 0
            searched_bias = round(random.uniform(-5, 5), 2)
            
            for inpt in self.inputs:
                
                searched_weight = round(random.uniform(-5, 5), 2)
                output += inpt * searched_weight
                
                searched_weights.append(searched_weight)
                
            output += searched_bias
            output = round(output, 1)
            iteration += 1
            
            print(iteration ," Iteration ", self.inputs, searched_weights, searched_bias, " Output ", output)
            
        return [self.inputs, searched_weights, searched_bias]
                    

n = [3.0, 2.1, 2.17, 3.18]
w_out = 2.0
                
searched_out = Training(n, w_out)
searched_out.train()
            
            
            