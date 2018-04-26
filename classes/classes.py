class Line:
    """This is a class which contains all trajectories (i.e. all railways used).

        Args:
            trajectoryList (list): list of trajectories.
    """

    def __init__(self, trajectoryList):
        self.trajectoryList = trajectoryList

    def SLine(self, criticalRailwayList):
        """Function that determines S for Trajectory

        Args:
            criticalRailwayList (list): List of all railways that are critical.

        Returns:
            Total amount of minutes (min), amount of trains used (t),
            percentage of critical railways used (p) and the scorefunction
            S = 10000*p - (t*20 + min/10).
        """
        self.criticalRailwayList = criticalRailwayList
        minutes = 0
        trains = 0
        criticalRailway = []

        for Trajectory in self.trajectoryList:
            minutes += Trajectory.minutesTrajectory()
            trains += 1

        # looks for all critical railways in trajectory and puts them in a list
        for Trajectory in self.trajectoryList:
            for Rail in Trajectory.__dict__.items():
                for Railtje in Rail[1]:
                    if Railtje not in criticalRailway:
                        if Railtje in self.criticalRailwayList:
                            criticalRailway.append(Railtje)

        p = len(criticalRailway) / len(self.criticalRailwayList)

        return ['min = {}'.format(minutes),
            't = {}'.format(trains), 'p = {}'.format(p),
            'S = {}'.format(10000 * p - (trains * 20 + minutes / 10)) ]

class Trajectory:
    """Class which contains railways used.

    Args:
        raillist (list): List of railways.
    """
    def __init__(self, raillist):
        self.raillist = raillist

        # checks if all railways are really connected
        for i in range(len(self.raillist) - 1):
            if (self.raillist[i].stationBeginning != self.raillist[i+1].stationBeginning
                and self.raillist[i].stationEnd != self.raillist[i+1].stationEnd
                and self.raillist[i].stationBeginning != self.raillist[i+1].stationEnd
                and self.raillist[i].stationEnd != self.raillist[i+1].stationBeginning):
                    print('Error: cannot make Trajectory')
                    print(self.raillist[i].stationBeginning)
                    print(self.raillist[i+1].stationBeginning)
                    break

    def minutesTrajectory(self):
        """Function that determines total amount of minutes of all railways."""
        minutes = 0
        for station in self.raillist:
            if station is not '':
                minutes += station.minutes
        return minutes

class Rail:
    """Class of a rail between stations.

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
    """Class of stations

    Args:
        name (str): Name of stations.
        x (float): x-coördinate of station's location.
        y (float): y-coördinate of station's location.
        Critical (str): Input 'Kritiek' when station is critical and an empty
                        string ('') when not critical.
    """
    def __init__(self, name, x, y, critical):
        self.name = name
        self.x = x
        self.y = y
        self.Critical = critical
