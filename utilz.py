#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 08:26:17 2021

@author: ortoc
"""

class isLooked():
    
    def __init__(self,L1,L2,B1,B2):
     self.B1 = B1 # x0, y0
     self.B2 = B2 # x1, y1
     self.B3 = [B1[0],B2[1]] # x0, y1
     self.B4 = [B2[0],B1[1]] # x1, y0
     self.L1 = L1
     self.L2 = L2
    
    def ccw(self,A,B,C):
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
    
    # Return true if line segments AB and CD intersect
    def intersect(self,L1,L2,B1,B2):

        return self.ccw(L1,B1,B2) != self.ccw(L2,B1,B2) and self.ccw(L1,L2,B1) != self.ccw(L1,L2,B2)
    
    def bbox(self):
        L1=self.L1
        L2=self.L2
        B1=self.B1
        B2=self.B2
        B3=self.B3
        B4=self.B4
        
        return (self.intersect(L1,L2,B1,B3) | self.intersect(L1,L2,B3,B2) | self.intersect(L1,L2,B2,B4) | self.intersect(L1,L2,B1,B4)) == True
