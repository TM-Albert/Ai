# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:34:41 2023

@author: Albert
"""

class ML:
    
    def __init__(self):
        pass
    
    def transform(self, arrayToTransform):
        
        n = len(arrayToTransform[0])
        transformedArray = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                
               transformedArray[j][i] = arrayToTransform[i][j]
                

        return transformedArray
    
    def shorterVersionOfTransform(self, arrayToTransform):
        
        n = len(arrayToTransform[0])
        transformedArray = [[arrayToTransform[j][i] for j in range(n)] for i in range(n)]
        
        return transformedArray
        
        
ml = ML()

MA = [[4, 2, 6, 9],
     [7, 5, 1, 7],
     [6, 2, 0, 11],
     [2, 11, 12, 9]]

print(MA)

shorter_MA = ml.shorterVersionOfTransform(MA)
transformed_MA = ml.transform(MA)

print(shorter_MA)
print(transformed_MA)