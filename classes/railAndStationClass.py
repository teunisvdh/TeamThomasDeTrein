import random
import sys
import operator
import numpy as np
import numpy.random as rn
from algorithms import randomAlgorithm
from algorithms import SimulatedAnnealing
from classes import lineClass
from classes import trajectoryClass
from classes import railAndStationClass
from classes import helpers
sys.path.append('C:/TeamThomasDeTrein/classes')

class Rail:
    """
    Class of a rail between stations.

    Args:
        stationBeginning (str): Station where rail begins.
        stationEnd (str): Station where rail ends.
        minutes (int): Minutes needed to get from the beginning to end of the rail.
    """
    def __init__(self, stationBeginning, stationEnd, minutes):
        self.stationBeginning = stationBeginning
        self.stationEnd = stationEnd
        self.minutes = int(minutes)


class Station:
    """Class of stations.

    Args:
        name (str): Name of stations.
        x (float): x-coördinate of station's location.
        y (float): y-coördinate of station's location.
        Critical (str): Input 'Kritiek' when station is critical
            and an empty string ('') when not critical.
    """
    def __init__(self, name, x, y, Critical):
        self.name = name
        self.x = x
        self.y = y
        self.Critical = Critical
