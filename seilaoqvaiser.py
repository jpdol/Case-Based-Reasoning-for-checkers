# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:11:56 2018

@author: Luiz Carlos
"""

import pandas as pd
import numpy as np
import random as rd
from winnerVerification import *

def verifyDir(nextMove):
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
  captureP = []
  captureD = []
  countP = 0
  countD = 0
  for i, row in enumerate(boardState):
      for j, space in enumerate(row):
          if space == 'wp':
              captureP.append(seeNeighbors(i, j, boardState, captureP))
          elif space == 'wd':
              captureD.append(seeNeighborsDama(i, j, boardState, captureD))
          else:
              pass
  for space in captureP:
    if len(space)>2:
      countP = countP+1
  for space in captureD:
    if len(space)>2:
      countD = countD+1
  if countP <= 0:
    captureP = None
  if countD <= 0:
    captureD = None
  return captureP, captureD

def verifyMovement(startPos, endPos, hDir, vDir, board, typeOfPiece):
  if board[startPos[0]][startPos[1]] == typeOfPiece and board[endPos[0]][endPos[1]] == 'no':
    return endPos
  elif board[startPos[0]][startPos[1]] == typeOfPiece and board[vDir*endPos[0]][hDir*endPos[1]] == 'no':
    print([vDir*endPos[0], hDir*endPos[1]])
    return [vDir*endPos[0], hDir*endPos[1]]
  elif board[startPos[0]][startPos[1]] == typeOfPiece and board[vDir*endPos[0]][-hDir*endPos[1]] == 'no':
    print([vDir*endPos[0], -hDir*endPos[1]])
    return [vDir*endPos[0], -hDir*endPos[1]]
  else:
    print(3)
    return None

def lookForPiece(board, startPos, hDir, vDir, typeOfPiece):
  i = 0
  j = 0
  board[startPos[0]][startPos[1]] = 'done'
  print(board)
  while(i < 8):
    randDirline = rd.choice([-1,1])
    j = 0
    while(j < 7):
      randDircol = rd.choice([-1,1])
      if startPos[0] + randDirline* i < 8 and startPos[0] + randDirline* i >= 0:
        if startPos[1] + randDircol*j < 8 and startPos[1] + randDircol*j >= 0:
          if board[startPos[0] + randDirline* i][startPos[1] + randDircol*j] == typeOfPiece:
            check = verifyMovement([startPos[0] + randDirline* i, startPos[1] + randDircol*j] , [startPos[0] + randDirline* i+1, startPos[1] + randDircol*j+1] ,randDircol, 1, board, typeOfPiece)
            if check is not None:
              return [[startPos[0] + randDirline* i, startPos[1] + randDircol*j], check]
            
        if startPos[1] - randDircol*j < 8 and startPos[1] - randDircol*j >= 0:
          if board[startPos[0] + randDirline* i][startPos[1] - randDircol*j] == typeOfPiece:
            check = verifyMovement([startPos[0] + randDirline* i, startPos[1] - randDircol*j], [startPos[0] + randDirline* i + 1, startPos[1] - randDircol*j+1] ,-randDircol, 1, board, typeOfPiece)
            if check is not None:
              return [[startPos[0] + randDirline* i, startPos[1] - randDircol*j], check]
            
      if startPos[0] - randDirline* i < 8 and startPos[0] - randDirline* i >= 0:
        if startPos[1] + randDircol*j < 8 and startPos[1] + randDircol*j >= 0:
          if board[startPos[0] - randDirline* i][startPos[1] + randDircol*j] == typeOfPiece:
            check = verifyMovement([startPos[0] - randDirline* i, startPos[1] + randDircol*j], [startPos[0] - randDirline* i + 1, startPos[1] + randDircol*j + 1] ,randDircol, 1, board, typeOfPiece)
            if check is not None:
              return [[startPos[0] - randDirline* i, startPos[1] + randDircol*j], check]
            
        if startPos[1] - randDircol*j < 8 and startPos[1] - randDircol*j >= 0:
          if board[startPos[0] - randDirline* i][startPos[1] - randDircol*j] == typeOfPiece:
            check = verifyMovement([startPos[0] - randDirline* i, startPos[1] - randDircol*j], [startPos[0] - randDirline* i + 1, startPos[1] - randDircol*j + 1] ,-randDircol, 1, board, typeOfPiece)
            if check is not None:
              return [[startPos[0] - randDirline* i, startPos[1] - randDircol*j], check]
      j = j+1
    i = i+1
  return None

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
        self.casesUsedList = []
    
    def simLocal(self, case, row, i):
                
        if row[i] == 'no':
            ci = 0
            weight = 0.5
        elif row[i] == 'wp':
            ci = 0.5
            weight = 0.5
        elif row[i] == 'wd':
            ci = 1
            weight = 0.5
        elif row[i] == 'bp':
            ci = -0.5
            weight = 0.5
        elif row[i] == 'bd':
            ci = -1
            weight = 0.5
        elif i == len(row)-2:
            ci = row[i]
            weight = 7
        elif i == len(row)-1:
            ci = row[i]
            weight = 8
        else:
            return None, None
        
        if case[i] == 'no':
            cf = 0
            weight = 0.5
        elif case[i] == 'wp':
            cf = 0.5
            weight = 0.5
        elif case[i] == 'wd':
            cf = 1
            weight = 0.5
        elif case[i] == 'bp':
            cf = -0.5
            weight = 0.5
        elif case[i] == 'bd':
            cf = -1
            weight = 0.5
        elif i == len(row)-2:
            cf = row[i]
            weight = 7
        elif i == len(row)-1:
            cf = row[i]
            weight = 8
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
    
    def closestSim(self):
      highest = self.globalSimList[0]
      index = 0
      for i, globalSim in enumerate(self.globalSimList):
        if highest < globalSim:
          highest = globalSim
          index = i
      
      return highest, index
    
    def avaliation(self,newCasesList, result):
      if result== 'win':
        att = 1.1
        
      elif result == 'lose':
        att = 0.9
      else:
        att = 1
      
    
    def receiveAndAdapt(self,case): #case eh uma lista
      board = []
      for row in range(8):
          lin = []
          for column in range(8):
              lin.append(case[column+(8*row)])
          board.append(lin)
      
      checkForCaptureP, checkForCaptureD = hasCapture(board)
      
      longestMove = None
      index = 0
      if checkForCaptureP is not None:
        longestMove = checkForCaptureP[0]
        # print(checkForCaptureP)
        for i, out in enumerate(checkForCaptureP):
          if len(out) > len(longestMove):
            longestMove = out
            index = i
      if checkForCaptureD is not None:
        longestMove = checkForCaptureD[0]
        for i, out in enumerate(checkForCaptureD):
          if len(out) > len(longestMove):
            longestMove = out
            index = i
            
      if longestMove is not None:
        resultAdapt = ''
        char = 0
        while char <= len(longestMove)-1:
          resultAdapt = resultAdapt + chr(longestMove[char+1]+97) + str(longestMove[char] + 1) + 'x'
          char = char+2
        return resultAdapt[:len(resultAdapt)-1]
      
      #verificar casos
      self.simGlobal(case)
      highest, index = self.closestSim()
      self.casesUsedList.append(index)
      outB = self.out.loc[index][0]
      startPos = [ord(outB[0]) - 97, int(outB[1]) - 1]
      outB = self.out.loc[index][0]
      startPos = [ord(outB[0]) - 97, int(outB[1]) - 1]
      endPos = [ord(outB[3]) - 97, int(outB[4]) - 1]
      typeOfPiece = self.caseBase.loc[index][outB[0]+outB[1]]
      hDir, vDir = verifyDir(outB)
      nextSpace = verifyMovement(startPos, endPos, hDir, vDir, board, typeOfPiece)
      if nextSpace is not None:
        return nextSpace
      else:
        return lookForPiece(board, startPos, hDir, vDir, typeOfPiece)

    # n = cbr.adapt(current_board)
    # n = cbr.adapt(['no',None,'wp',None,'wp',None,'no',None,None,'wp',None,'wp',None,'no',None,'wp','no',None,'wp',None,'no',None,'wp',None,None,'bp',None,'no',None,'wp',None,'wp','bp',None,'no',None,'bp',None,'no',None,None,'no',None,'bp',None,'bp',None,'bp','bp',None,'no',None,'no',None,'no',None,None,'no',None,'bp',None,'no',None,'bp',0,0.75])
    # print(n)    