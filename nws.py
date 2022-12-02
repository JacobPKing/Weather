# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:35:13 2022

@author: jacob
"""
import requests
import json

class NWS:
    
    @staticmethod
    def makeRequest(req:str) -> dict:
        print(f'Making request: {req} ', end = '')
        request = requests.get('https://api.weather.gov/{}'.format(req))
        print('done')
        return json.loads(request.text)
        
    @staticmethod
    def isValidReply(reply:dict) -> bool:
        return 'status' not in reply.keys()