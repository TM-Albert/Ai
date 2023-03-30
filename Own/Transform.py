# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:34:41 2023

@author: Albert
"""

class ML:
    
    def __init__(self):
        return
    
    def transform(self, arrayToTransform):
        
        n = len(arrayToTransform[0])
        transformedArray = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                
                transformedArray[j][i] = arrayToTransform[i][j]
                

        return transformedArray
        
ml = ML()

MA = [[4, 2, 6, 9],
     [7, 5, 1, 7],
     [6, 2, 0, 11],
     [2, 11, 12, 9]]

print(MA)

ml.transform(MA)