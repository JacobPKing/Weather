# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:34:11 2022

@author: jacob
"""
import numpy as np

class Coords:
    
    earthRadiusM = 6371000
    
    def __init__(self, lat:float, long:float):
        self.lat = lat
        self.long = long
        
    def toList(self):
        return [self.lat, self.long]
    
    def distance(self, other):
        return Coords.dist(self.toList(), other.toList())
    
    def __repr__(self):
        return f'<{self.lat}, {self.long}>'
    
    @staticmethod
    def dist(clist1,clist2) -> float:
        lat1 = clist1[0] * np.pi/180
        lat2 = clist2[0] * np.pi/180
        long1 = clist1[1] * np.pi/180
        long2 = clist2[1] * np.pi/180
        dlong = long2 - long1
        return np.arccos(np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(lat2) * np.cos(dlong)) * 6371000 / 1000