# -*- coding: utf-8 -*-
"""
Class that contains information regarding weather stations
Member variables:
    code: 4 letter symbol that denotes a station
    lat: latitude
    long: longitude
    coords: Coords object, used for distance


Created on Tue Sep 27 22:33:23 2022

@author: jacob
"""

from nws import NWS
from coords import Coords
from jtime import JTime
import numpy as np
import matplotlib.pyplot as plt

class Station:
    
    def __init__(self, code:str):
        self.code = code
        self.info = NWS.makeRequest(f'stations/{self.code}')
        # print(self.info)
        self.long = self.info['geometry']['coordinates'][0]
        self.lat = self.info['geometry']['coordinates'][1]
        self.coords = Coords(self.lat, self.long)
        self.obervations = None
        
    def __repr__(self):
        return self.code
        
    def getWeather(self):
        if self.obervations is None:
            self.observations = NWS.makeRequest(f'stations/{self.code}/observations')
            self.observations = self.observations['features']
            
        tempsarr = np.empty([0,0])
        timesarr = np.empty([0,0])
            
        for obs in self.observations:
            timestamp = obs['id'][-25:-6]
            print(timestamp)
            print(JTime.timeAgo(timestamp))
            print(obs['properties']['temperature']['value'])
            timesarr = np.append(timesarr, JTime.timeAgo(timestamp))
            tempsarr = np.append(tempsarr, obs['properties']['temperature']['value'])
            print("-------------------------")
            
        print(timesarr)
        print(tempsarr)
        
        plt.plot(timesarr, tempsarr)
        plt.title("Temperature")
        plt.xlabel('Hours ago')
        plt.ylabel("Temp (C)")
            
        return self.obervations
        
