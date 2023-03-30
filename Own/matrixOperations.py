# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:48:41 2023

@author: Albert
"""

MA = [[4, 2, 6, 9],
     [7, 5, 1, 7],
     [6, 2, 0, 11],
     [2, 11, 12, 9]]

MB = [[7, 2, 4, 8],
     [6, 5, 9, 7],
     [1, 7, 4, 1],
     [0, 1, 2, 0]]


ML = len(MA[0])
MC =[[0 for j in range(ML)] for i in range(ML) ]

for i in range(ML):
    MARow = MA[i]
    
    for j in range(ML):
        MCRowElement = 0
        
        for z in range(ML):
            
            MCRowElement += MARow[j] * MB[z][0]
            
        MC[i][j] = MCRowElement
        
        
print(MC)



        
        
            