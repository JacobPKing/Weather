# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:29:52 2022

@author: jacob
"""

from location import Location

b = Location(38,-82)
#print(b.stations)
print(b.stations[2])
for n in range(1,5):
    b.stations[n].getWeather()


#print(b.stations[1].info)