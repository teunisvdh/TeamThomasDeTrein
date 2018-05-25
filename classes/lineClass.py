import random
import sys
import os
import operator
import numpy as np
import numpy.random as rn
from algorithms import randomAlgorithm
from algorithms import SimulatedAnnealing
from classes import trajectoryClass
from classes import railAndStationClass
from classes import helpers
from classes import lineClass
directory = os.path.dirname(os.getcwd())
sys.path.append(directory + '/TeamThomasDeTrein/classes')

class Line:
    """This is a class which contains  a list of all trajectories used,
        the list of all railways in general, the list of all critical railways and
        an inverse dictionairy which pairs each railway and it's inverse

    Args:
        TrajectoryList (list): list of trajectories
        RailwayList (list): list of all railways
        criticalRailwayList (list): list of all critical railways
        inverseDict (dict): a dict where rails and their inverses are paired
    """

    def __init__(self, TrajectoryList, RailwayList, criticalRailwayList, inverseDict):
        self.TrajectoryList = TrajectoryList
        self.RailwayList = RailwayList
        self.criticalRailwayList = criticalRailwayList
        self.inverseDict = inverseDict

    def SLine(self):
        """Function that determines S = 10000 * p  - (trains * 20 + minutes / 10)
            for Trajectory, where p is percentage of critical railways used, trains
            is amount of trajectories used and minutes is total amount of minutes of
            the whole line.

        Returns:
             Scorefunction (S)
        """
        minutes = 0
        trains = 0
        criticalRailway = []

        for Trajectory in self.TrajectoryList:
            minutes += Trajectory.minutesTrajectory()
            trains += 1

        count = 0

        # iterate over each trajectory and make a list of all critical railways used
        for Trajectory in self.TrajectoryList:
            for Railtje in Trajectory.Raillist:
                if Railtje not in criticalRailway and self.inverseDict[Railtje] not in criticalRailway:
                    if Railtje in self.criticalRailwayList:
                        criticalRailway.append(Railtje)

        p = len(criticalRailway) / (len(self.criticalRailwayList) / 2)

        return 10000 * p  - (trains * 20 + minutes / 10)

    def lenLine(self):
        """ Function that determines amount of trajectories in line.

        Returns:
            Amount of trajectories
        """
        return len(self.TrajectoryList)

    def translateTrajectByNumber(self, number):
        """ Function that selects a trajectory.

        Args:
            number (int): Number of the trajectory you want to select

        Returns:
            Trajectory on that number in list
        """
        self.number = number
        return self.TrajectoryList[self.number]

    def selectRandomTrajectory(self):
        """ Function that selects random trajectory in line.

        Returns:
            Random trajectory
        """
        chooseRandomTrajectory = random.randint(0, self.lenLine() - 1)
        RandomTrajectory = self.translateTrajectByNumber(chooseRandomTrajectory)
        return RandomTrajectory

    def removeTrajectByTrajectory(self, trajectory):
        """ Function that removes a trajectory from a line
        """
        self.trajectory = trajectory
        self.TrajectoryList.remove(self.trajectory)

    def addTrajectByTrajectory(self, trajectory):
        """ Function that adds a trajectory to a line
        """
        # add a random trajectory
        self.trajectory = trajectory
        self.TrajectoryList.append(self.trajectory)

    def updateTrajectoryList(self):
        """ Function that determines the list of trajectories in a line.

        Returns:
            List of trajectories
        """
        trajectoryList = []
        for traject in self.TrajectoryList:
            trajectoryList.append(traject)

        return trajectoryList

    def addHighestRailInTrajectory(self, startTrajectory):
        """ Function that adds in a trajectory a rail that gives the highest score
            for the line.

        Args:
            startTrajectory (Trajectory): Trajectory to which you want to add the rail
        """
        listOfScores = {}

        for rail in startTrajectory.RailwayList:

            # add and delete rails and keep the scores in a dict
            startTrajectory.addRailbyRailBeginning(rail)
            self.addTrajectByTrajectory(startTrajectory)
            score = self.SLine()
            listOfScores[rail] = score
            self.removeTrajectByTrajectory(startTrajectory)
            startTrajectory.removeRailbyRailBeginning()

            # select the highest score and corresponding rail
            highestRail = (max(listOfScores.items(), key=operator.itemgetter(1))[0])
            highestScore = (max(listOfScores.items(), key=operator.itemgetter(1))[1])

        # add rail that gives highest score
        startTrajectory.addRailbyRailEnd(highestRail)

    def determineRailsBeginEnd(self, startTrajectory):
        """ Function that makes lists of rails that can be added to beginning and
            end of trajectory.

        Args:
            startTrajectory (Trajectory): Trajectory in which you want to find
                corresponding rails
        Returns:
            listOfScoresBeginning (list): List of all rails that can be added to
                the beginning of the traject
            listOfScoresEnd (list): List of all rails that can be added to
                the end of the traject
        """
        listOfScoresEnd = {}
        listOfScoresBeginning = {}

        # find all corresponding rails
        possibleRails = startTrajectory.correspondingRails()

        for rail in possibleRails:

            # check if rail can be added to beginning of trajectory
            if startTrajectory.trajectBeginStation == rail.stationEnd:
                startTrajectory.addRailbyRailBeginning(rail)
                self.addTrajectByTrajectory(startTrajectory)
                score_2 = self.SLine()
                listOfScoresBeginning[rail] = score_2
                self.removeTrajectByTrajectory(startTrajectory)
                startTrajectory.removeRailbyRailBeginning()

            # check if rail can be added to end of trajectory
            if startTrajectory.trajectEndStation == rail.stationBeginning:
                startTrajectory.addRailbyRailEnd(rail)
                self.addTrajectByTrajectory(startTrajectory)
                score_2 = self.SLine()
                listOfScoresEnd[rail] = score_2
                self.removeTrajectByTrajectory(startTrajectory)
                startTrajectory.removeRailbyRailEnd()

        return listOfScoresBeginning, listOfScoresEnd

    def checkScoreAndChoppedScore(self, startTrajectory):
        """ Function that checks score of trajectory in line for whole trajectory
            and for the trajectory with a rail removed

        Args:
            startTrajectory (Trajectory): Trajectory for which you want to determine
            score.
        Returns:
            score: Score of whole trajectory
            choppedScore: Score of trajectory with removed rail element
        """

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
        """ Function that makes replaces a trajectory for either a random trajectory
            or a snake trajectory if score gets higher.

        Args:
            trajectory (Trajectory): Trajectory that you want to replace
            stepSize (int): Amount of iterations you want to use for the random/snake
                trajectory
            replace (string): Input "random" if you want to replace for random trajectory,
                "snake" otherwise
        """
        # score without change
        score = self.SLine()

        # make copy of trajectory
        tempTrajectory = trajectoryClass.Trajectory([], self.RailwayList)
        for rail in trajectory.Raillist:
            tempTrajectory.addRailbyRailEnd(rail)

        self.removeTrajectByTrajectory(trajectory)

        # make change
        if replace == "random":
            replaceTrajectory = randomAlgorithm.randomTrajectory(tempTrajectory, stepSize)
        if replace == "snake":
            replaceTrajectory = SimulatedAnnealing.makeSnakeTrajectory(self, tempTrajectory, stepSize)

        self.addTrajectByTrajectory(replaceTrajectory)

        # score with change
        score_2 = self.SLine()

        self.removeTrajectByTrajectory(replaceTrajectory)

        # if score gets higher
        if score_2 > score:

            # make the change
            self.addTrajectByTrajectory(replaceTrajectory)

        else:

            # otherwise dont make the change
            self.addTrajectByTrajectory(trajectory)

    def determineScoreWithTrajectory(self, startTrajectory):
        """ Function that determines score if a given trajectory would be added

        Args:
            startTrajectory (Trajectory): Trajectory that you want to determine
                score for

        Returns:
            score
        """
        self.addTrajectByTrajectory(startTrajectory)
        score = self.SLine()
        self.removeTrajectByTrajectory(startTrajectory)

        return score

    def scoreWithAndWithoutTrajectory(self, newTrajectory):
        """ Function that determines score if a given trajectory would be added
                and score if not

        Args:
            startTrajectory (Trajectory): Trajectory that you want to determine
                score for

        Returns:
            score with trajectory, score without trajectory
        """

        score = self.SLine()
        self.removeTrajectByTrajectory(newTrajectory)
        score_2 = self.SLine()

        return score, score_2

    def scoreWithTrajectory(self, newTrajectory):
        """ Function that adds trajectory and determine score

        Args:
            newTrajectory (Trajectory): Trajectory that you want to determine
                score for

        Returns:
            score with trajectory
        """
        # add trajectory to line
        self.addTrajectByTrajectory(newTrajectory)

        # determine score again
        score_3 = self.SLine()

        return score_3

    def addToUnfullLine(self, maxAmountOfTrajectories, replace, amountOfRails):
        """ Function that adds trajectories to a line that is not full yet

        Args:
            maxAmountOfTrajectories (int): Maximum amount of trajectories you want to add
            replace (string): "random" for adding with random algorithm, "snake" for
                snake algorithm
            amountOfRails (int): Amount of rails you want to add per trajectory
        """

        # check if line is full
        if self.lenLine() < maxAmountOfTrajectories:

            # determine score
            score_4 = self.SLine()

            # add a new random trajectory
            newTrajectory = self.makeReplace(replace, amountOfRails)

            self.addTrajectByTrajectory(newTrajectory)

            # determine score
            score_5 = self.SLine()

            # if score is not higher, remove trajectory
            if score_4 > score_5:
                self.removeTrajectByTrajectory(newTrajectory)

    def makeReplace(self, replace, amountOfRails):
        """ Function that makes a trajectory to replace

        Args:
            replace (string): "random" for adding with random algorithm, "snake" for
                snake algorithm
            amountOfRails (int): Amount of rails you want to add per trajectory
        """
        if replace == "random":
            replaceTrajectory = randomAlgorithm.emptyRandom(self, amountOfRails)

        if replace == "snake":
            emptyTrajectory = trajectoryClass.Trajectory([], self.RailwayList)
            replaceTrajectory = SimulatedAnnealing.makeSnakeTrajectory(self, emptyTrajectory, 15)

        return replaceTrajectory

    def replace(self, replace, trajectory, stepSize):
        """ Function that replaces a trajectory for a random/snake trajectory

        Args:
            replace (string): "random" for replicing with random algorithm, "snake" for
                snake algorithm
            trajectory (Trajectory): Trajectory which you want to change
            stepSize (int): Amount of iterations you want to use for random/snake
                algorithm
        """
        if replace == "random":
            self.replaceTrajectory(trajectory, stepSize, "random")
        if replace == "snake":
            self.replaceTrajectory(trajectory, stepSize, "snake")
