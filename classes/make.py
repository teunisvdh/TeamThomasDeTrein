import csv
import sys
import os
from data import *
from classes import classes

def makeLine1(RailwayList):

	# define the trajectory
	trajectory1 = classes.Trajectory([RailwayList[1], RailwayList[0], RailwayList[27], RailwayList[25], RailwayList[10]])
	trajectory2 = classes.Trajectory([RailwayList[3], RailwayList[4], RailwayList[5], RailwayList[17]])
	trajectory3 = classes.Trajectory([RailwayList[12], RailwayList[21], RailwayList[23]])
	trajectory4 = classes.Trajectory([RailwayList[15], RailwayList[19], RailwayList[13]])
	trajectory5 = classes.Trajectory([RailwayList[16], RailwayList[26], RailwayList[27]])
	trajectory6 = classes.Trajectory([RailwayList[14], RailwayList[22], RailwayList[24], RailwayList[11], RailwayList[6]])

	line1 = [trajectory1, trajectory2, trajectory3, trajectory4, trajectory5, trajectory6]
	return line1
