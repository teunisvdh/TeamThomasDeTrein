import random
import sys
from algorithms import randomAlgorithm

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
            correspondingStations = []
            # list of all possible connections
            correspondingStations = self.correspondingRails()

            # takes random rail and appends possible Raillist
            randomIndex = random.randint(0, len(correspondingStations) - 1)
            randomRail = correspondingStations[randomIndex]

            # if rail is connected at beginning traject, beginTraject wil be stationEnd of new rail
            if self.trajectBeginStation == randomRail.stationBeginning:
                self.Raillist.insert(0, randomRail)
                minutes = self.minutesTrajectory()
                if minutes > 120:
                    self.Raillist.pop(0)
                else:
                    self.trajectBeginStation = randomRail.stationEnd

            # if rail is connected at end traject, endTraject will be station End of new rail
            elif self.trajectEndStation == randomRail.stationBeginning:
                self.Raillist.append(randomRail)
                minutes = self.minutesTrajectory()
                if minutes > 120:
                    self.Raillist.pop()
                else:
                    self.trajectEndStation = randomRail.stationEnd



    def correspondingRails(self):
        correspondingStations = []

        # checks for RailwayList of beginTraject or EndTraject connections
        for rail in self.RailwayList:
            if self.trajectBeginStation == rail.stationBeginning:
                correspondingStations.append(rail)
            elif self.trajectEndStation == rail.stationBeginning:
                correspondingStations.append(rail)

        return correspondingStations

    def addRailbyRailEnd(self,rail):
        self.rail = rail
        self.Raillist.append(self.rail)

        return self.Raillist

    def addRailbyRailBeginning(self,rail):
        self.rail = rail
        self.Raillist.insert(0, self.rail)

        return self.Raillist

    def removeRailbyRail(self,rail):
        self.rail = rail
        self.Raillist.remove(self.rail)

        return self.Raillist






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
