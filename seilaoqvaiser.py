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
    #print(boardstate)
    capturePos = [i,j]
    if (i-1 >= 0 and j-1 >= 0) or (i+1 < 8 and j+1 < 8) or (i-1>=0 and j+1<8) or (i+1<8 and j-1>=0):
        if boardstate[i-1][j-1] == 'bp' or boardstate[i-1][j-1] == 'bd':
            if  i-2 >= 0 and j-2 >=0:
                if boardstate[i-2][j-2] == 'no' or boardstate[i-2][j-2] == 'no':
                    temp = boardstate[i][j]
                    newBoardState = boardstate
                    newBoardState[i][j] = 'no'
                    newBoardState[i-2][j-2] = temp
                    newBoardState[i-1][j-1] = 'bt'
                    capturePos=capturePos+seeNeighbors(i-2, j-2, newBoardState, capturePos)
                else:
                    pass
        if i+2 < 8 and j+2 < 8:
            if boardstate[i+1][j+1] == 'bp' or boardstate[i+1][j+1] == 'bd':
                if boardstate[i+2][j+2] == 'no' or boardstate[i+2][j+2] == 'no':
                    temp = boardstate[i][j]
                    newBoardState = boardstate
                    newBoardState[i][j] = 'no'
                    newBoardState[i+2][j+2] = temp
                    newBoardState[i+1][j+1] = 'bt'
                    print(i,j)
                    capturePos=capturePos+seeNeighbors(i+2, j+2, newBoardState, capturePos)
                else:
                    pass
        if i-2 >= 0 and j+2 < 8:
            if boardstate[i-1][j+1] == 'bp' or boardstate[i-1][j+1] == 'bd':
                if boardstate[i-2][j+2] == 'no' or boardstate[i-2][j+2] == 'no':
                    temp = boardstate[i][j]
                    newBoardState = boardstate
                    newBoardState[i][j] = 'no'
                    newBoardState[i-2][j+2] = temp
                    newBoardState[i-1][j+1] = 'bt'
                    capturePos=capturePos+seeNeighbors(i-2, j+2, newBoardState, capturePos)
                else:
                    pass
        if i+2 < 8 and j-2 >= 0:
            if boardstate[i+1][j-1] == 'bp' or boardstate[i+1][j-1] == 'bd':
                if boardstate[i+2][j-2] == 'no' or boardstate[i+2][j-2] == 'no':
                    temp = boardstate[i][j]
                    newBoardState = boardstate
                    newBoardState[i][j] = 'no'
                    newBoardState[i+2][j-2] = temp
                    newBoardState[i+1][j-1] = 'bt'
                    capturePos=capturePos+seeNeighbors(i+2, j-2, newBoardState, capturePos)
                else:
                    pass
        
        return capturePos

def seeNeighborsDama(i, j, boardState, capturePos):
    right = 6-j
    left = j+1
    up = i+1
    down = 6-i
    capturePos = [i,j]
    #checking up right
    for index in range(np.min([up,right])):
        if boardState[i-1-index][j+1+index] == 'bp' or boardState[i-1-index][j+1+index] == 'bd':
            if boardState[i-index-2][j+index+2] == 'no' or boardState[i-index-2][j+index+2] == 'no':
                    temp = boardState[i][j]
                    newBoardState = boardState
                    newBoardState[i][j] = 'no'
                    newBoardState[i-index-2][j+index+2] = temp
                    newBoardState[i-index-1][j+index+1] = 'bt'
                    capturePos=capturePos+seeNeighborsDama(i-index-2, j+index+2, newBoardState, capturePos)
            else:
                pass
    #check up left
    for index in range(np.min([up, left])):
        if boardState[i-1-index][j-1-index] == 'bp' or boardState[i-1-index][j-1-index] == 'bd':
            if boardState[i-index-2][j-index-2] == 'no' or boardState[i-index-2][j-index-2] == 'no':
                    temp = boardState[i][j]
                    newBoardState = boardState
                    newBoardState[i][j] = 'no'
                    newBoardState[i-index-2][j-index-2] = temp
                    newBoardState[i-index-1][j-index-1] = 'bt'
                    capturePos=capturePos+seeNeighborsDama(i-index-2, j-index-2, newBoardState, capturePos)
            else:
                pass
    #check down left
    for index in range(np.min([down, left])):
        if boardState[i+1+index][j-1-index] == 'bp' or boardState[i+1+index][j-1-index] == 'bd':
            if boardState[i+index+2][j-index-2] == 'no' or boardState[i+index+2][j-index-2] == 'no':
                    temp = boardState[i][j]
                    newBoardState = boardState
                    newBoardState[i][j] = 'no'
                    newBoardState[i+index+2][j-index-2] = temp
                    newBoardState[i+index+1][j-index-1] = 'bt'
                    capturePos=capturePos+seeNeighborsDama(i+index+2, j-index-2, newBoardState, capturePos)
            else:
                pass
    #check down right
    for index in range(np.min([down, right])):
        if boardState[i+1+index][j+1+index] == 'bp' or boardState[i+1+index][j+1+index] == 'bd':
            if boardState[i+index+2][j+index+2] == 'no' or boardState[i+index+2][j+index+2] == 'no':
                    temp = boardState[i][j]
                    newBoardState = boardState
                    newBoardState[i][j] = 'no'
                    newBoardState[i+index+2][j+index+2] = temp
                    capturePos=capturePos+seeNeighborsDama(i+index+2, j+index+2, newBoardState, capturePos)
            else:
                pass
    return capturePos

def hasCapture(boardState):
    capture = []
    for i, row in enumerate(boardState):
        for j, space in enumerate(row):
            if space == 'wp':
                capture.append(seeNeighbors(i, j, boardState, capture))
            elif space == 'wd':
                capture.append(seeNeighborsDama(i, j, boardState, capture))
            else:
                pass
    return capture

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
        for i, globalSim in enumerate(self.globalSimList):
            if highest < globalSim:
                highest = globalSim
                index = i
        outB = self.out.loc[index][0]
        board = []
        for row in range(8):
            lin = []
            for column in range(8):
                lin.append(case[column+(8*row)])
            board.append(lin)
        return hasCapture(board)
        
        startPos = [ord(outB[0]) - 97, int(outB[1]) - 1]
        
    
if __name__ == "__main__":
    dataset = pd.read_csv(r"C:\Users\7\Desktop\smartchess\Case-Based-Reasoning-for-chess\CaseBase\caseBase.csv")
    #(h, v) = verifyDirs(dataset.loc[1,'next_move'])
    out = pd.DataFrame(dataset.loc[:,'next_move'])
    dataset = dataset.drop("next_move", axis = 1)
    cbr = CBR(dataset, out)
    cbr.simGlobal(['wp',None,'wp',None,'wp',None,'wp',None,None,'wp',None,'wp',None,'wp',None,'wp','wp',None,'no',None,'wp',None,'wp',None,None,'wp',None,'no',None,'no',None,'no','no',None,'no',None,'bp',None,'no',None,None,'bp',None,'no',None,'bp',None,'bp','bp',None,'bp',None,'bp',None,'bp',None,None,'bp',None,'bp',None,'bp',None,'bp',0,0.75])
    #cbr.adapt(['wp',None,'wp',None,'wp',None,'wp',None,None,'wp',None,'wp',None,'wp',None,'wp','wp',None,'no',None,'wp',None,'wp',None,None,'wp',None,'no',None,'no',None,'no','no',None,'no',None,'bp',None,'no',None,None,'bp',None,'no',None,'bp',None,'bp','bp',None,'bp',None,'bp',None,'bp',None,None,'bp',None,'bp',None,'bp',None,'bp',0,0.75])
    #k = cbr.adapt(['wp',None,'wp',None,'wp',None,'wp',None,None,'wp',None,'wp',None,'wp',None,'wp','wp',None,'no',None,'wp',None,'wp',None,None,'bp',None,'no',None,'no',None,'no','bp',None,'no',None,'no',None,'no',None,None,'no',None,'no',None,'bp',None,'bp','bp',None,'bp',None,'bp',None,'bp',None,None,'bp',None,'bp',None,'bp',None,'bp'])
    cbr.simGlobal(['no',None,'wp',None,'wp',None,'wp',None,None,'no',None,'no',None,'no',None,'no','wp',None,'bp',None,'no',None,'no',None,None,'no',None,'no',None,'bp',None,'no','no',None,'no',None,'no',None,'no',None,None,'no',None,'wd',None,'bp',None,'bp','no',None,'no',None,'no',None,'bp',None,None,'no',None,'no',None,'no',None,'bp',1,0.75])
    
    
    