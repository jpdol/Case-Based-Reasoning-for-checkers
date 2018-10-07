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

def seeNeighbors(i, j, boardstate, capturePos):
    if (i-1 >= 0 and j-1 >= 0) or (i+1 < 8 and j+1 < 8) or (i-1>=0 and j+1<8) or (i+1<8 and j-1>=0):
        if boardstate[i-1][j-1] == 'bp' or boardstate[i-1][j-1] == 'bd':
            if  i-2 >= 0 and j-2 >=0:
                if boardstate[i-2][j-2] == 'no' or boardstate[i-2][j-2] == 'no':
                    capturePos.append([i-3, j-3])
                    temp = boardstate[i][j]
                    newBoardState = boardstate
                    newBoardState[i][j] = 'no'
                    newBoardState[i-3][j-3] = temp
                    seeNeighbors(i-3, j-3, newBoardState, capturePos)
                else:
                    pass
        if i+2 < 8 and j+2 < 8:
            if boardstate[i+1][j+1] == 'bp' or boardstate[i+1][j+1] == 'bd':
                if boardstate[i+2][j+2] == 'no' or boardstate[i+2][j+2] == 'no':
                    capturePos.append([i+3, j+3])
                    temp = boardstate[i][j]
                    newBoardState = boardstate
                    newBoardState[i][j] = 'no'
                    newBoardState[i+3][j+3] = temp
                    seeNeighbors(i+3, j+3, newBoardState, capturePos)
                else:
                    pass
        if i-2 >= 0 and j+2 < 8:
            if boardstate[i-1][j+1] == 'bp' or boardstate[i-1][j+1] == 'bd':
                if boardstate[i-2][j+2] == 'no' or boardstate[i-2][j+2] == 'no':
                    capturePos.append([i-3, j-3])
                    temp = boardstate[i][j]
                    newBoardState = boardstate
                    newBoardState[i][j] = 'no'
                    newBoardState[i-3][j-3] = temp
                    seeNeighbors(i-3, j-3, newBoardState, capturePos)
                else:
                    pass

def hasCapture(boardState):
    capture = []
    for i, row in enumerate(boardState):
        for j, space in enumerate(row):
            if space == 'wp':
                seeNeighbors(i, j, boardState, capture)
                        

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
    def __init__(self, caseBase, out):
        self.caseBase = caseBase
        self.out = out
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
            return None, None
        
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
            return None, None
        
        return np.max([0, 1 - np.abs(ci - cf)]), weight
    
    def simGlobal(self, case):
        for index, row in self.caseBase.iterrows():
            weightSet = 0
            simPort = 0
            for i in range(len(row)):
                (simLocal,weight) = self.simLocal(case, row, i)
                if(simLocal != None or weight != None):
                    weightSet = weightSet+weight
                    simPort = simPort + (simLocal*weight)
            self.globalSimList.append(simPort/weightSet)
    
    def adapt(self,case): #case eh uma lista
        highest = self.globalSimList[0]
        index = 0
        for i, globalSim in self.globalSimList:
            if highest < globalSim:
                highest = globalSim
                index = i
        outB = self.out.loc[index][0]
        board = []
        for space in case:
            row = []
            for i in range(8):
                row.append(i)
            board.append(row)
        hasCapture()
        startPos = [ord(outB[0]) - 97, int(outB[1]) - 1]
        
    
if __name__ == "__main__":
    dataset = pd.read_csv(r"C:\Users\7\Desktop\smartchess\Case-Based-Reasoning-for-chess\CaseBase\caseBase.csv")
    #(h, v) = verifyDirs(dataset.loc[1,'next_move'])
    out = pd.DataFrame(dataset.loc[:,'next_move'])
    dataset = dataset.drop("next_move", axis = 1)
    cbr = CBR(dataset, out)
    cbr.simGlobal(['wp',None,'wp',None,'wp',None,'wp',None,None,'wp',None,'wp',None,'wp',None,'wp','wp',None,'no',None,'wp',None,'wp',None,None,'wp',None,'no',None,'no',None,'no','no',None,'no',None,'bp',None,'no',None,None,'bp',None,'no',None,'bp',None,'bp','bp',None,'bp',None,'bp',None,'bp',None,None,'bp',None,'bp',None,'bp',None,'bp',0,0.75])
    