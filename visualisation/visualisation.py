import csv, sys, os, random
import matplotlib.pyplot as plt
import matplotlib.lines as lin
import sys
sys.path.append('C:/TeamThomasDeTrein/classes')
sys.path.append('C:/TeamThomasDeTrein/algorithms')
from algorithms import randomAlgorithm
from classes import helpers
# from matplotlib import colors as col

# color library for coloring lines
# colors = []
# for color in col.CSS4_COLORS:
#     colors.append(color)
def visualize(maxRail, stationList, RailwayList):
    """ A function for plotting a graph (map) visualizing a line of railways.

        Args:
            maxRail: line with maximum score (determined by an algorithm).
    """
    returnPlotMap = plotMap(stationList, RailwayList)
    mapConnection(returnPlotMap)
    lineConnection(maxRail, returnPlotMap)
    makePlot(maxRail)


def plotMap(stationList, RailwayList):
    """ Opens lists and plots all stations in map.
    """
    # plot all stations
    for station in stationList:
        x = float(station.y)
        y = float(station.x)
        plt.plot(x, y, 'ro-')
        plt.annotate(station.name, xy=(x,y))
    return RailwayList, stationList

def connect(begin, end, stationList):
    """ A function for connecting two stations in a plot.

        Args:
            begin = station beginning, end = station end
    """
    nameBegin = begin
    nameEnd = end
    # stationList = RailwayList[1]
    for i in range(len(stationList)):
        if (stationList[i].name == nameBegin):
            x1=float(stationList[i].y)
            y1=float(stationList[i].x)
            break
    for i in range(len(stationList)):
        if (stationList[i].name == nameEnd):
            x2=float(stationList[i].y)
            y2=float(stationList[i].x)
            break
    plt.plot([x1, x2], [y1, y2], 'k-', linewidth=0.2)

# plot all connections
def mapConnection(returnPlotMap):
    """ A function for plotting all railways between stations.

        Args:
            returnPlotMap: RailwayList, stationList.
    """
    RailwayList = returnPlotMap[0]
    stationList = returnPlotMap[1]
    for connection in RailwayList:
        connect(connection.stationBeginning, connection.stationEnd, stationList)

def connectLine(begin, end, returnPlotMap, style, label):
    """ A function for connecting two stations in a plot, specifically
        for the whole line.

        Args:
            begin = station beginning, end = station end,
            style = color and style line
    """
    nameBegin = begin
    nameEnd = end
    styleLine = style
    stationList = returnPlotMap[1]
    distance = random.uniform(0, 0.001)
    for i in range(len(stationList)):
        if (stationList[i].name == nameBegin):
            x1=float(stationList[i].y)
            y1=float(stationList[i].x) + distance
            break
    for i in range(len(stationList)):
        if (stationList[i].name == nameEnd):
            x2=float(stationList[i].y)
            y2=float(stationList[i].x) + distance
            break
    plt.plot([x1, x2], [y1, y2], styleLine, linewidth=1, label=label)


def lineConnection(maxRail, returnPlotMap):
    """ A function for plotting the assigned connections between stations (line).

        Args:
            maxRail: line with maximum score (determined by an algorithm).
            returnPlotMap: RailwayList, stationList.
    """
    lineStyle = ['r-.', 'r:', 'g-.', 'g:', 'c-.', 'c:', 'm-.', 'm:', 'y-.', 'y:', 'b-.', 'b:']
    # connect rails in all trajectories
    for i in range(len(maxRail.TrajectoryList)):
        style = random.choice(lineStyle)
        # style = random.choice(colors)
        # lineStyle.remove(style)
        label = str(i+1)
        for j in range(len(maxRail.TrajectoryList[i].Raillist)):
            if j == 0:
                connectLine(maxRail.TrajectoryList[i].Raillist[j].stationBeginning, maxRail.TrajectoryList[i].Raillist[j].stationEnd, returnPlotMap, style, label)
            else:
                connectLine(maxRail.TrajectoryList[i].Raillist[j].stationBeginning, maxRail.TrajectoryList[i].Raillist[j].stationEnd, returnPlotMap, style, '')


        # plt.legend([connected], "bla")

def makePlot(maxRail):
    """ Shows the plot.
    """
    # make plot
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.title("Line with score " + str(maxRail.SLine()), ha='center')
    # plt.suptitle("Line Visualisation", ha='center')
    plt.axis('equal')
    # axis = plt.gca();
    # axis.text(5.2, 51.78, "Score: " + str(maxRail.SLine()), ha='left')
    plt.legend()
    plt.show()

def printLine(maxRail):
    """ A function for printing a line.

        Args:
            maxRail: line with maximum score (determined by an algorithm).
    """
    for i in range(len(maxRail.TrajectoryList)):
        print("")
        print("Traject {}".format(i+1))
        print("---------")
        for j in range(len(maxRail.TrajectoryList[i].Raillist)):
            print(maxRail.TrajectoryList[i].Raillist[j].stationBeginning)
            print(maxRail.TrajectoryList[i].Raillist[j].stationEnd)
