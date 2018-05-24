import random
import sys
import operator
import numpy as np
import numpy.random as rn
from algorithms import randomAlgorithm
from algorithms import SimulatedAnnealing

sys.path.append('C:/TeamThomasDeTrein/classes')

class Line:
    """This is a class which contains all trajectories (i.e. all railways used).

    Args:
        trajectoryList (list): list of trajectories.

    Functions:
        Sline(self,criticalRailwayList).
    """

    def __init__(self, TrajectoryList, RailwayList, criticalRailwayList, inverseDict):
        self.TrajectoryList = TrajectoryList
        self.RailwayList = RailwayList
        self.criticalRailwayList = criticalRailwayList
        self.inverseDict = inverseDict

    def SLine(self):
        """Function that determines S for Trajectory.

        Args:
        criticalRailwayList (list): List of all railways that are critical.

        Returns:
        Total amount of minutes (min), amount of trains used (t),
        percentage of critical railways used (p) and the scorefunction
        S = 10000*p - (t*20 + min/10).
        """
        minutes = 0
        trains = 0
        criticalRailway = []

        for Trajectory in self.TrajectoryList:
            minutes += Trajectory.minutesTrajectory()
            trains += 1

        count = 0

        for Trajectory in self.TrajectoryList:
            for Railtje in Trajectory.Raillist:
                if Railtje not in criticalRailway and self.inverseDict[Railtje] not in criticalRailway:
                    if Railtje in self.criticalRailwayList:
                        criticalRailway.append(Railtje)

        p = len(criticalRailway) / (len(self.criticalRailwayList) / 2)

        alles = ['min = {}'.format(minutes),
            't = {}'.format(trains), 'p = {}'.format(p),
            'S = {}'.format(10000 * p - (trains * 20 + minutes / 10)) ]

        return 10000 * p  - (trains * 20 + minutes / 10)

    def lenLine(self):
        return len(self.TrajectoryList)

    def translateTrajectByNumber(self, number):
        self.number = number
        return self.TrajectoryList[self.number]

    def selectRandomTrajectory(self):
        chooseRandomTrajectory = random.randint(0, self.lenLine() - 1)
        RandomTrajectory = self.translateTrajectByNumber(chooseRandomTrajectory)
        return RandomTrajectory

    def removeTrajectByTrajectory(self, trajectory):
        self.trajectory = trajectory
        self.TrajectoryList.remove(self.trajectory)

        return self.TrajectoryList

    def addTrajectByTrajectory(self, trajectory):
        # add a random trajectory
        self.trajectory = trajectory
        self.TrajectoryList.append(self.trajectory)

        return self.TrajectoryList

    def updateTrajectoryList(self):
        trajectoryList = []
        for traject in self.TrajectoryList:
            trajectoryList.append(traject)

        return trajectoryList

    def addHighestRailInTrajectory(self, startTrajectory):
        listOfScores = {}

        for rail in startTrajectory.RailwayList:
            # if rail is connected at beginning traject, beginTraject wil be stationEnd of new rail
            startTrajectory.addRailbyRailBeginning(rail)
            self.addTrajectByTrajectory(startTrajectory)
            score = self.SLine()
            listOfScores[rail] = score
            self.removeTrajectByTrajectory(startTrajectory)
            startTrajectory.removeRailbyRailBeginning()

            highestRail = (max(listOfScores.items(), key=operator.itemgetter(1))[0])
            highestScore = (max(listOfScores.items(), key=operator.itemgetter(1))[1])

        startTrajectory.addRailbyRailEnd(highestRail)

    def addTrajectoryAndDetermineCorrespondingRails(self, startTrajectory):
        listOfScoresEnd = {}
        listOfScoresBeginning = {}
        possibleRails = startTrajectory.correspondingRails()
        for rail in possibleRails:
            # if rail is connected at beginning traject, beginTraject wil be stationEnd of new rail
            if startTrajectory.trajectBeginStation == rail.stationEnd:
                startTrajectory.addRailbyRailBeginning(rail)
                self.addTrajectByTrajectory(startTrajectory)
                score_2 = self.SLine()
                listOfScoresBeginning[rail] = score_2
                self.removeTrajectByTrajectory(startTrajectory)
                startTrajectory.removeRailbyRailBeginning()

            if startTrajectory.trajectEndStation == rail.stationBeginning:
                startTrajectory.addRailbyRailEnd(rail)
                self.addTrajectByTrajectory(startTrajectory)
                score_2 = self.SLine()
                listOfScoresEnd[rail] = score_2
                self.removeTrajectByTrajectory(startTrajectory)
                startTrajectory.removeRailbyRailEnd()

        return listOfScoresBeginning, listOfScoresEnd

    def checkScoreAndChoppedScore(self, startTrajectory):
        self.addTrajectByTrajectory(startTrajectory)
        score = self.SLine()
        self.removeTrajectByTrajectory(startTrajectory)

        startRail = startTrajectory.Raillist[0]
        startTrajectory.removeRailbyRailBeginning()

        self.addTrajectByTrajectory(startTrajectory)
        choppedScore = self.SLine()
        self.removeTrajectByTrajectory(startTrajectory)

        startTrajectory.addRailbyRailBeginning(startRail)

        return score, choppedScore

    def replaceTrajectory(self, trajectory, stepSize, replace):
        score = self.SLine()
        tempTrajectory = Trajectory([], self.RailwayList)
        for rail in trajectory.Raillist:
            tempTrajectory.addRailbyRailEnd(rail)
        self.removeTrajectByTrajectory(trajectory)
        if replace == "random":
            replaceTrajectory = randomAlgorithm.randomTrajectory(tempTrajectory, stepSize)
        if replace == "snake":
            replaceTrajectory = SimulatedAnnealing.makeSnakeTrajectory(self, tempTrajectory, stepSize)
        self.addTrajectByTrajectory(replaceTrajectory)
        score_2 = self.SLine()
        self.removeTrajectByTrajectory(replaceTrajectory)

        if score_2 > score:
            self.addTrajectByTrajectory(replaceTrajectory)

        else:
            self.addTrajectByTrajectory(trajectory)

    def determineScoreWithTrajectory(self, startTrajectory):
        self.addTrajectByTrajectory(startTrajectory)
        score = self.SLine()
        self.removeTrajectByTrajectory(startTrajectory)

        return score

    def scoreWithAndWithoutTrajectory(self, RandomTrajectory):
        # determine score
        score = self.SLine()

        # remove random trajectory
        self.removeTrajectByTrajectory(RandomTrajectory)

        # determine score again
        score_2 = self.SLine()

        return score, score_2

    def scoreWithTrajectory(self, replaceTrajectory):
        # add trajectory to line
        self.addTrajectByTrajectory(replaceTrajectory)

        # determine score again
        score_3 = self.SLine()

        return score_3

    def addToUnfullLine(self, maxAmountOfTrajectories):
        # check if line is full
        if self.lenLine() < maxAmountOfTrajectories:

            # determine score
            score_4 = self.SLine()

            # add a new random trajectory
            newTrajectory = randomAlgorithm.emptyRandom(self)
            self.addTrajectByTrajectory(newTrajectory)

            # determine score
            score_5 = self.SLine()

            # if score is not higher, remove trajectory
            if score_4 > score_5:
                self.removeTrajectByTrajectory(newTrajectory)


class Trajectory:
    """
    Class which contains railways used.

    Args:
        raillist (list): List of railways.
    """
    def __init__(self, Raillist, RailwayList):
        self.Raillist = Raillist
        self.RailwayList = RailwayList
        self.trajectBeginStation = None
        self.trajectEndStation = None


        if len(self.Raillist) > 0:
            self.trajectBeginStation = Raillist[0].stationBeginning
            self.trajectEndStation = Raillist[-1].stationEnd

        for i in range(len(self.Raillist) - 1):
            if (self.Raillist[i].stationBeginning != self.Raillist[i+1].stationBeginning
                and self.Raillist[i].stationEnd != self.Raillist[i+1].stationEnd
                and self.Raillist[i].stationBeginning != self.Raillist[i+1].stationEnd
                and self.Raillist[i].stationEnd != self.Raillist[i+1].stationBeginning):
                    print('Error: cannot make Trajectory')
                    print(self.Raillist[i].stationBeginning)
                    print(self.Raillist[i+1].stationBeginning)
                    break

    # calculates total amount of minutes for each Trajectory
    def minutesTrajectory(self):
        """Function that calculates total minutes of trajectory.

        Args:
            raillist (list): List of railways.

        Returns:
            total minutes of trajectory.
        """
        minutes = 0
        for station in self.Raillist:
                minutes += station.minutes
        # if minutes > 120:
            # print("to much minutes!")
        return minutes

    def addRail(self):
        """Function that adds a random rail to the trajectory.
        """
        # add a random connection
        randomIndex = random.randint(0, len(self.RailwayList) - 1)
        randomRail = self.RailwayList[randomIndex]

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
                if minutes > 180:
                    self.Raillist.pop(0)
                else:
                    self.trajectBeginStation = randomRail.stationBeginning

            # if rail is connected at end traject, endTraject will be station End of new rail
            elif self.trajectEndStation == randomRail.stationBeginning:
                self.Raillist.append(randomRail)
                minutes = self.minutesTrajectory()
                if minutes > 180:
                    self.Raillist.pop()
                else:
                    self.trajectEndStation = randomRail.stationEnd

    def correspondingRails(self):
        correspondingStations = []
        # checks for RailwayList of beginTraject or EndTraject connections
        for rail in self.RailwayList:
            if self.trajectBeginStation == rail.stationEnd:
                correspondingStations.append(rail)
            elif self.trajectEndStation == rail.stationBeginning:
                correspondingStations.append(rail)

        return correspondingStations

    def addRailbyRailEnd(self,rail):
        self.rail = rail
        if len(self.Raillist) == 0:
            self.trajectBeginStation = self.rail.stationBeginning
            self.trajectEndStation = self.rail.stationEnd
        else:
            self.trajectEndStation = self.rail.stationEnd

        self.Raillist.append(self.rail)

        return self.Raillist

    def addRailbyRailBeginning(self,rail):
        self.rail = rail
        if len(self.Raillist) == 0:
            self.trajectBeginStation = self.rail.stationBeginning
            self.trajectEndStation = self.rail.stationEnd
        else:
            self.trajectBeginStation = self.rail.stationBeginning

        self.Raillist.insert(0, self.rail)

        return self.Raillist

    def removeRailbyRailEnd(self):
        if len(self.Raillist) != 0:
            if len(self.Raillist) == 1:
                self.trajectEndStation = None
                self.trajectBeginStation = None
            else:
                self.trajectEndStation = self.Raillist[-1].stationBeginning

            self.Raillist.pop()

        return self.Raillist

    def removeRailbyRailBeginning(self):
        if len(self.Raillist) != 0:
            if len(self.Raillist) == 1:
                self.trajectEndStation = None
                self.trajectBeginStation = None
            else:
                self.trajectBeginStation = self.Raillist[0].stationEnd

            self.Raillist.remove(self.Raillist[0])

        return self.Raillist

    def simAnnealingAdd(self, var, score, randomScore, T, randomRail):
        if SimulatedAnnealing.acceptance(score, randomScore, 10*T) == True:
            if self.minutesTrajectory() < 180:
                if var == "begin":
                    self.addRailbyRailBeginning(randomRail)
                if var == "end":
                    self.addRailbyRailEnd(randomRail)

    def simAnnealingChop(self, line, T):
        if len(self.Raillist) > 1:
            score, choppedScore = line.checkScoreAndChoppedScore(self)

            if SimulatedAnnealing.acceptance(score, choppedScore,  10 * T) > rn.random():
                self.removeRailbyRailBeginning()







        # make a list of all connections that can be added
        # if StationIsBeginning == True:
        #     for rail in self.RailwayList:
        #         if self.Raillist[-1].stationBeginning == rail.stationBeginning:
        #             correspondingStations.append(rail)
        #         elif self.Raillist[-1].stationBeginning == rail.stationEnd:
        #             correspondingStations.append(rail)
        #     randomRailNext = random.randint(0, len(correspondingStations) - 1)
        #     if correspondingStations[randomRailNext].stationBeginning == self.Raillist[-1].stationBeginning:
        #         StationIsBeginning = False
        #     else:
        #         StationIsBeginning = True
        #
        # elif StationIsBeginning == False:
        #     for rail in self.RailwayList:
        #         if self.Raillist[-1].stationEnd == rail.stationBeginning:
        #             correspondingStations.append(rail)
        #         elif self.Raillist[-1].stationEnd == rail.stationEnd:
        #             correspondingStations.append(rail)
        #     randomRailNext = random.randint(0, len(correspondingStations) - 1)
        #     if correspondingStations[randomRailNext].stationEnd == self.Raillist[-1].stationEnd:
        #         StationIsBeginning = True
        #     else:
        #         StationIsBeginning = False
        #
        # return randomRailNext, correspondingStations



    def Pop(self):
        """Function that deletes the last rail in the trajectory.
        """
        self.Raillist.pop()

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
