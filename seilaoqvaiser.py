# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:11:56 2018

@author: Luiz Carlos
"""

import pandas as pd

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
    
    def similLocal:
        
        

if __name__ == "__main__":
    dataset = pd.read_csv(r"C:\Users\7\Desktop\smartchess\Case-Based-Reasoning-for-chess\checkersgame1.csv")
    (h, v) = verifyDirs(dataset.loc[1,'next_move'])
    