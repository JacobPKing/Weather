#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import datetime
import time
"""
Class containing static methods to help with timestamps

For this class, all timestamps are given in terms of UTC in the following format
2022-09-22T04:55:00
YYYY-MM-DDTHH:MM:SS
"""
class JTime:
    
    @staticmethod
    def isWithin(ts1:str, ts2:str, length:float) -> bool:
        """
        Returns true if timestamp2 is within *length* hours of timestamp1, inclusive
        Ex: (2022-09-22T04:55:00, 2022-09-22T05:55:00, 1) -> true
            (2022-09-22T04:55:00, 2022-09-22T03:55:00, 1) -> true
            (2022-09-22T04:55:00, 2022-09-22T05:56:00, 1) -> false
        Parameters
        ----------
        timestamp1 : str
        timestamp2 : str
        length : float
        Returns
        -------
        bool
        """
        return abs(JTime.timeDifference(ts1, ts2)) <= length
    
    @staticmethod
    def timeDifference(ts1:str, ts2:str) -> float:
        """
        Returns the difference in hours between 2 timestamps as a float
        Ex: (2022-09-22T04:55:00, 2022-09-22T05:55:00) -> 1
            (2022-09-22T04:55:00, 2022-09-22T03:55:00) -> -1
        Parameters
        ----------
        timestamp1 : str
        timestamp2 : str

        Returns
        -------
        float
        """
        return (JTime.ts2unix(ts2) - JTime.ts2unix(ts1)) / 3600

    def timeAgo(ts:str) -> float:
        """
        Returns how many hours ago a timestamp is

        Parameters
        ----------
        ts : str
            DESCRIPTION.

        Returns
        -------
        float
            DESCRIPTION.

        """
        return(time.mktime(datetime.datetime.utcnow().timetuple()) - JTime.ts2unix(ts)) / 3600

    @staticmethod
    def ts2list(ts:str) -> list:
        return re.split('-|:|T',ts)
    
    @staticmethod
    def ts2unix(ts:str) -> int:
        tslist = JTime.ts2list(ts)
        tslist = [int(x) for x in tslist]
        dtime = datetime.datetime(tslist[0],tslist[1],tslist[2],tslist[3],tslist[4],tslist[5])
        return time.mktime(dtime.timetuple())