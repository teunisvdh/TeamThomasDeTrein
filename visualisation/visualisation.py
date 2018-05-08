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
def visualize(maxRail):
    # make list with all stations
    # maxRail = randomAlgorithm()
    stationList, criticalstationList = helpers.openFile.file1("data/StationsHolland.csv")
    RailwayList, criticalRailwayList = helpers.openFile.file2("data/ConnectiesHolland.csv", criticalstationList)

    # plot all stations
    def plotStations():
        for station in stationList:
            x = float(station.y)
            y = float(station.x)
            plt.plot(x, y, 'ro-')
            plt.annotate(station.name, xy=(x,y))

    plotStations()

    def connect(begin, end):
        """ A function for connecting two stations in a plot.

            Args:
                begin = station beginning, end = station end
        """
        nameBegin = begin
        nameEnd = end
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
    for connection in RailwayList:
        connect(connection.stationBeginning, connection.stationEnd)

    def connectLine(begin, end, style):
        """ A function for connecting two stations in a plot, specifically
            for the whole line.

            Args:
                begin = station beginning, end = station end,
                style = color and style line
        """
        nameBegin = begin
        nameEnd = end
        styleLine = style
        distance = random.uniform(0, 0.01)
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
        plt.plot([x1, x2], [y1, y2], styleLine, linewidth=2)

    lineStyle = ['r-.', 'r:', 'g-.', 'g:', 'c-.', 'c:', 'm-.', 'm:', 'y-.', 'y:', 'b-.', 'b:']

    # Connect rails in all trajectories
    for i in range(len(maxRail)):
        print("")
        print("Traject {}".format(i+1))
        print("---------")
        # print(highestRail[i])
        style = random.choice(lineStyle)
        # style = random.choice(colors)
        lineStyle.remove(style)
        for j in range(len(maxRail[i].Raillist)):
            print(maxRail[i].Raillist[j].stationBeginning)
            print(maxRail[i].Raillist[j].stationEnd)
            connectLine(maxRail[i].Raillist[j].stationBeginning, maxRail[i].Raillist[j].stationEnd, style)

    # make plot
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.title("Visualisation")
    plt.axis('equal')
    plt.show()
