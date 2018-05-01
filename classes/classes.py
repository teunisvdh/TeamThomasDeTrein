class Line:
"""
This is a class which contains all trajectories (i.e. all railways used).

Args:
trajectoryList (list): list of trajectories.

Functions:
Sline(self,criticalRailwayList).
"""
    def __init__(self, TrajectoryList):
        self.TrajectoryList = TrajectoryList

    def SLine(self, criticalRailwayList):
    """
    Function that determines S for Trajectory.

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

        return ['min = {}'.format(minutes),
            't = {}'.format(trains), 'p = {}'.format(p),
            'S = {}'.format(10000 * p - (trains * 20 + minutes / 10)) ]

class Trajectory:
"""
Class which contains railways used.

Args:
raillist (list): List of railways.
"""
    def __init__(self, Raillist):
        self.Raillist = Raillist

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
    """
    Function that calculates total minutes of trajectory
    
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
"""
Class of stations

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
