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

    def __init__(self, TrajectoryList, RailwayList, criticalRailwayList):
        self.TrajectoryList = TrajectoryList
        self.RailwayList = RailwayList
        self.criticalRailwayList = criticalRailwayList

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

        # print("########")
        # print(self.RailwayList)
        # print("########")
        # print(self.criticalRailwayList)
        # print("########")

        # adds minutes of each railway in trajectory to minutes
        for Trajectory in self.TrajectoryList:
            minutes += Trajectory.minutesTrajectory()
            trains += 1

        # looks for all critical railways in trajectory and puts them in a list
        for Trajectory in self.TrajectoryList:
            for Rail in Trajectory.__dict__.items():
                for Railtje in Rail[1]:
                    if Railtje not in criticalRailway:
                        if Railtje in self.criticalRailwayList:
                            criticalRailway.append(Railtje)

        p = len(criticalRailway) / len(self.criticalRailwayList)

        alles = ['min = {}'.format(minutes),
            't = {}'.format(trains), 'p = {}'.format(p),
            'S = {}'.format(10000 * p - (trains * 20 + minutes / 10)) ]

        return 10000 * p - (trains * 20 + minutes / 10)

    def lenLine(self):
        return len(self.TrajectoryList)

    def translateTrajectByNumber(self, number):
        self.number = number
        return self.TrajectoryList[self.number]

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
        if minutes > 120:
            print("to much minutes!")
        return minutes

    def addRail(self):
        # add a random connection
        randomRail = random.randint(0, len(self.RailwayList) - 1)
        self.Raillist.append(self.RailwayList[randomRail])

    def addConnections(self):

        StationIsBeginning = True

        # add a random amount more connections
        amountOfRails = random.randint(1,10)

        for amount in range(amountOfRails):
            correspondingStations = []
            # make a list of all connections that can be added
            if StationIsBeginning == True:
                for rail in self.RailwayList:
                    if self.Raillist[-1].stationBeginning == rail.stationBeginning:
                        correspondingStations.append(rail)
                    elif self.Raillist[-1].stationBeginning == rail.stationEnd:
                        correspondingStations.append(rail)
                randomRailNext = random.randint(0, len(correspondingStations) - 1)
                if correspondingStations[randomRailNext].stationBeginning == self.Raillist[-1].stationBeginning:
                    StationIsBeginning = False
                else:
                    StationIsBeginning = True

            elif StationIsBeginning == False:
                for rail in self.RailwayList:
                    if self.Raillist[-1].stationEnd == rail.stationBeginning:
                        correspondingStations.append(rail)
                    elif self.Raillist[-1].stationEnd == rail.stationEnd:
                        correspondingStations.append(rail)
                randomRailNext = random.randint(0, len(correspondingStations) - 1)
                if correspondingStations[randomRailNext].stationEnd == self.Raillist[-1].stationEnd:
                    StationIsBeginning = True
                else:
                    StationIsBeginning = False

            self.Raillist.append(correspondingStations[randomRailNext])

            minutes = 0
            for station in self.Raillist:
                    minutes += station.minutes

            if minutes > 120:
                self.Raillist.pop()

    def Pop(self):
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
