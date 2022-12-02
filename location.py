# -*- coding: utf-8 -*-
"""
For now this is the main driving class. Most things should be done through a
specific location.
Member variables:
    lat: latitude
    long: longitude, will be negative numbner
    isInit: if the init method has been run yet (not constructor)
    info: dictionary with various info about the coordinates selection
    stations: list of nearby station objects


Created on Tue Sep 27 22:30:34 2022

@author: jacob
"""

from nws import NWS
from station import Station
from coords import Coords
import json
import requests

class Location:
    
    def __init__(self, lat:float, long:float):
        self.coords = Coords(lat, long)
        self.lat = lat
        self.long = long
        self.init()
        
    def init(self):
        # Get overall info
        self.info = NWS.makeRequest('points/{},{}'.format(self.lat, self.long))
        if not NWS.isValidReply(self.info):
            raise Exception("Invalid location")
        
        #Get nearby observation stations
        nearbyStationsLink = self.info['properties']['observationStations']
        nearbyStationsReply = json.loads(requests.get(nearbyStationsLink).text)
        nearbyStationsList = nearbyStationsReply['observationStations']
        temp = []
        for stationLink in nearbyStationsList:
            temp.append(Station(stationLink[-4:]))
        self.stations = temp
        self.isInit = True
        
    def __repr__(self):
        return f'[Location at: {self.lat}, {self.long}]' if self.isInit else  f'[Needs init: {self.lat}, {self.long}]'