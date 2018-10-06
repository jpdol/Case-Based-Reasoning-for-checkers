# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:11:56 2018

@author: Luiz Carlos
"""
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
    def __init__(self):
        dist = 1
        dama = 0
        

if __name__ == "__main__":
    pass