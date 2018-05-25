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

class Trajectory:
    """
    Class which contains a list of railways used and a list of all railways

    Args:
        Raillist (list): List of railways used
        RailwayList (list): List of all railways
    """
    def __init__(self, Raillist, RailwayList):
        self.Raillist = Raillist
        self.RailwayList = RailwayList
        self.trajectBeginStation = None
        self.trajectEndStation = None


        if len(self.Raillist) > 0:

            # set begin and end of trajectory
            self.trajectBeginStation = Raillist[0].stationBeginning
            self.trajectEndStation = Raillist[-1].stationEnd

        # check if trajectory can be made, if not raise error
        for i in range(len(self.Raillist) - 1):
            if (self.Raillist[i].stationBeginning != self.Raillist[i+1].stationBeginning
                and self.Raillist[i].stationEnd != self.Raillist[i+1].stationEnd
                and self.Raillist[i].stationBeginning != self.Raillist[i+1].stationEnd
                and self.Raillist[i].stationEnd != self.Raillist[i+1].stationBeginning):
                    raise ValueError('Trajectory cannot be made')
                    break

    def minutesTrajectory(self):
        """Function that calculates total minutes of trajectory.

        Returns:
            total minutes of trajectory.
        """
        minutes = 0
        for station in self.Raillist:
                minutes += station.minutes

        return minutes

    def addRail(self):
        """Function that adds a random rail to the trajectory.
        """

        # add a random connection
        randomIndex = random.randint(0, len(self.RailwayList) - 1)
        randomRail = self.RailwayList[randomIndex]

        # update beginning and end of trajectory
        self.trajectBeginStation = randomRail.stationBeginning
        self.trajectEndStation = randomRail.stationEnd

        self.Raillist.append(randomRail)

    def addConnections(self, maxAmountOfRails):
        """Function that adds a random amount of rail connections to the line,
        with a given maximum.

        Args:
            maxAmountOfRails (int): Maximum amount of rails you want to add. The
            added amount of rails will be a number between zero and this number.
        """
        # add a random amount more connections
        self.amountOfRails = maxAmountOfRails

        for amount in range(self.amountOfRails):

            # list of all possible connections
            correspondingStations = self.correspondingRails()

            # takes random rail and appends possible Raillist
            randomIndex = random.randint(0, len(correspondingStations) - 1)
            randomRail = correspondingStations[randomIndex]

            # if rail is connected at beginning traject, beginTraject wil be stationEnd of new rail
            if self.trajectBeginStation == randomRail.stationEnd:
                self.Raillist.insert(0, randomRail)
                minutes = self.minutesTrajectory()

                if minutes > helpers.Files.maxMinutes:
                    self.Raillist.pop(0)
                else:
                    self.trajectBeginStation = randomRail.stationBeginning

            # if rail is connected at end traject, endTraject will be station End of new rail
            elif self.trajectEndStation == randomRail.stationBeginning:
                self.Raillist.append(randomRail)
                minutes = self.minutesTrajectory()

                if minutes > helpers.Files.maxMinutes:
                    self.Raillist.pop()
                else:
                    self.trajectEndStation = randomRail.stationEnd

    def correspondingRails(self):
        """ Function that determines rails that can be added to trajectory
        """
        correspondingStations = []

        # iterate over all railways
        for rail in self.RailwayList:

            # check if rail can be added to begin of trajectory
            if self.trajectBeginStation == rail.stationEnd:
                correspondingStations.append(rail)

            # check if rail can be added to end of trajectory
            elif self.trajectEndStation == rail.stationBeginning:
                correspondingStations.append(rail)

        return correspondingStations

    def addRailbyRailEnd(self,rail):
        """ Function that adds a rail to end of trajectory

        Args:
            rail (Rail): Rail element you want to add
        """

        self.rail = rail

        # update trajectories beginning and ending
        if len(self.Raillist) == 0:
            self.trajectBeginStation = self.rail.stationBeginning
            self.trajectEndStation = self.rail.stationEnd
        else:
            self.trajectEndStation = self.rail.stationEnd

        self.Raillist.append(self.rail)

        if self.minutesTrajectory() > helpers.Files.maxMinutes:
            self.removeRailbyRailEnd(self)

    def addRailbyRailBeginning(self, rail):
        """ Function that adds a rail to beginning of trajectory

        Args:
            rail (Rail): Rail element you want to add
        """

        self.rail = rail

        # update trajectories beginning and ending
        if len(self.Raillist) == 0:
            self.trajectBeginStation = self.rail.stationBeginning
            self.trajectEndStation = self.rail.stationEnd
        else:
            self.trajectBeginStation = self.rail.stationBeginning

        self.Raillist.insert(0, self.rail)

        if self.minutesTrajectory() > helpers.Files.maxMinutes:
            self.removeRailbyRailBeginning(self)



    def removeRailbyRailEnd(self):
        """ Function that removes a rail from end of trajectory
        """

        # update trajectories beginning and ending
        if len(self.Raillist) != 0:
            if len(self.Raillist) == 1:
                self.trajectEndStation = None
                self.trajectBeginStation = None
            else:
                self.trajectEndStation = self.Raillist[-1].stationBeginning

            self.Raillist.pop()

        return self.Raillist

    def removeRailbyRailBeginning(self):
        """ Function that removes a rail from beginning of trajectory
        """

        # update trajectories beginning and ending
        if len(self.Raillist) != 0:
            if len(self.Raillist) == 1:
                self.trajectEndStation = None
                self.trajectBeginStation = None
            else:
                self.trajectBeginStation = self.Raillist[0].stationEnd

            self.Raillist.remove(self.Raillist[0])

    def simAnnealingAdd(self, var, score, newScore, T, addRail, multiplicationAdd):
        """ Function that adds a rail to a trajectory with a certain probability
        generated by simmulated annealing.

        Args:
            var ("string"): "begin" if you want to beginning of trajectory, "end"
                if you want to add to end
            score (float): Score without rail added
            newScore (float): Score with rail added
            T (float): Temperature of annealing process
            addRail (Rail): Rail you want to add
            multiplicationAdd (float): Multiplication factor of T
        """
        if SimulatedAnnealing.acceptance(score, newScore, multiplication * T) == True:
            if self.minutesTrajectory() < helpers.Files.maxMinutes:
                if var == "begin":
                    self.addRailbyRailBeginning(addRail)
                if var == "end":
                    self.addRailbyRailEnd(addRail)

    def simAnnealingChop(self, line, T, multiplicationChop):
        """ Function that chops a rail from the beginning of trajectory with a
            probability generated by simmulated annealing.

        Args:
            line (Line): Line which contains trajectory
            T (float): Temperature of annealing process
            multiplicationChop (float): Multiplication factor of T
        """

        # only chop when there is more then one rail
        if len(self.Raillist) > 1:
            score, choppedScore = line.checkScoreAndChoppedScore(self)

            if SimulatedAnnealing.acceptance(score, choppedScore,  multiplication * T) == True:
                self.removeRailbyRailBeginning()

    def Pop(self):
        """Function that deletes the last rail in the trajectory.
        """
        self.Raillist.pop()
