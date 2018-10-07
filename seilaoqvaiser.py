# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:11:56 2018

@author: Luiz Carlos
"""

import pandas as pd
import numpy as np

def verifyDirs(nextMove):
    if nextMove[0] < nextMove[3]: #ie "a1-b2" a<b
        hdir = 1
    else:
        hdir = -1
    
    if nextMove[1] < nextMove[4]:
        vdir = 1
    else:
        vdir = -1
    
    return hdir, vdir

class piece:
    def __init__(self, kind):
        self.dist = 1
        self.dama = 0
        self.kind = kind

class board:
    def __init__(self):
        checkers = [[piece('wp'), None,piece('wp'), None,piece('wp'), None,piece('wp'), None],
                     [None, piece('wp'), None, piece('wp'), None, piece('wp'), None, piece('wp')],
                     [piece('wp'), None,piece('wp'), None,piece('wp'), None,piece('wp'), None],
                     [None, 'no', None, 'no', None, 'no', None, 'no'],
                     ['no', None, 'no', None, 'no', None, 'no', None],
                     [None, piece('bp'), None, piece('bp'), None, piece('bp'), None, piece('bp')],
                     [piece('bp'), None,piece('bp'), None,piece('bp'), None,piece('bp'), None],
                     [None, piece('bp'), None, piece('bp'), None, piece('bp'), None, piece('bp')]]
    

class CBR:
    def __init__(self, caseBase):
        self.caseBase = caseBase
        self.valueRange = [['no', 'wp', 'wd']]
        self.globalSimList = []
    
    def simLocal(self, case, row, i):
                
        if row[i] == 'no':
            ci = 0
            weight = 1
        elif row[i] == 'wp':
            ci = 0.5
            weight = 1
        elif row[i] == 'wd':
            ci = 1
            weight = 1
        elif row[i] == 'bp':
            ci = -0.5
            weight = 1
        elif row[i] == 'bd':
            ci = -1
            weight = 1
        elif i == len(row)-2:
            ci = row[i]
            weight = 7
        elif i == len(row)-1:
            ci = row[i]
            weight = 5
        else:
            pass
        
        if case[i] == 'no':
            cf = 0
            weight = 1
        elif case[i] == 'wp':
            cf = 0.5
            weight = 1
        elif case[i] == 'wd':
            cf = 1
            weight = 1
        elif case[i] == 'bp':
            cf = -0.5
            weight = 1
        elif case[i] == 'bd':
            cf = -1
            weight = 1
        elif i == len(row)-2:
            cf = row[i]
            weight = 7
        elif i == len(row)-1:
            cf = row[i]
            weight = 5
        else:
            pass
        
        return np.max([0, 1 - np.abs(ci - cf)]), weight
    
    def simGlobal(self, case):
        for index, row in self.caseBase.iterrows():
            for i in range(len(row)):
                (simLocal,weight) = self.simLocal(case, row, i)
            
        
    
if __name__ == "__main__":
    dataset = pd.read_csv(r"C:\Users\7\Desktop\smartchess\Case-Based-Reasoning-for-chess\checkersgame1.csv")
    #(h, v) = verifyDirs(dataset.loc[1,'next_move'])
    out = pd.DataFrame(dataset.loc[:,'next_move'])
    dataset = dataset.drop("next_move", axis = 1)
    u = dataset.iterrows()
    for index, row in dataset.iterrows():
        for i in range(len(row)):
            print(row[i])
        print('----------')
        
    