# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 00:55:24 2023

@author: Albert
"""

import random

class training:
    
    def __init__(self, inputs):
        self.inputs = inputs
        
    def train(self, wantedOutput):
        
        next_inputs = []
        
        for neuron in self.inputs:
            
            actual_inputs = neuron[0]
            searched_weights = []
            searched_weight = 0
            searched_bias = round(random.random(), 2)
            
            neuron_sum = 0
            
            for i in range(len(actual_inputs)):
                
                searched_weight = round(random.random(), 2)
                neuron_sum += actual_inputs[i] * searched_weight
                
                searched_weights.append(searched_weight)

                
            neuron_sum += searched_bias
            

            
                
                
            
            
            