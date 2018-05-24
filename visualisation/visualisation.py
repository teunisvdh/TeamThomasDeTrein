import csv, sys, os, random
import plotly as plly
import plotly.graph_objs as gob
directory = os.path.dirname(os.getcwd())
sys.path.append(directory + '/TeamThomasDeTrein/classes')
sys.path.append(directory + '/TeamThomasDeTrein/algorithms')

dataVisualise = []
mapbox_access_token='pk.eyJ1IjoidGV1bmlzdmRoIiwiYSI6ImNqaGdmNXBsczFicTkzNm82dWdxY3VzbDMifQ.-y7CGBStNzmzOpbnbRYFgg'


def visualize(maxRail, stationList, RailwayList):
    """ A function for plotting a graph (map) visualizing a line of railways.

        Args:
            maxRail: line with maximum score (determined by an algorithm).
    """
    returnPlotMap = plotMap(stationList, RailwayList)
    mapConnection(returnPlotMap)
    lineConnection(maxRail, returnPlotMap)
    makePlot(maxRail, returnPlotMap)

def plotMap(stationList, RailwayList):
    """ Opens lists and plots all stations in map.

        Args:
            stationList: list of all rail connections
            RailwayList: list of all stations

        Returns:
            RailwayList
            stationList
            data: Scattermapbox query of all stations
    """
    # plot all stations
    stationLat = []
    stationLon = []
    stationNames = []
    for station in stationList:
        x = float(station.y)
        y = float(station.x)
        stationLon.append(x)
        stationLat.append(y)
        stationNames.append(station.name)
    data = gob.Scattermapbox(lat=stationLat, lon=stationLon, mode='markers', marker=dict(size=7, color='red'), text=stationNames, name='Stations', legendgroup='Stations')
    return RailwayList, stationList, data

def connect(begin, end, stationList):
    """ A function for connecting two stations in a plot.

        Args:
            begin: station beginning
            end: station end
            stationList: list of all stations

        Returns:
            y1, y2, x1, x2 (coordinates)
    """
    nameBegin = begin
    nameEnd = end
    data = []
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
    return y1, y2, x1, x2

# plot all connections
def mapConnection(returnPlotMap):
    """ A function for plotting all railways between stations.

        Args:
            returnPlotMap: RailwayList, stationList, data
    """
    RailwayList = returnPlotMap[0]
    stationList = returnPlotMap[1]
    countLegend = 0
    for connection in RailwayList:
        y1, y2, x1, x2 = connect(connection.stationBeginning, connection.stationEnd, stationList)
        if (countLegend == 0):
            result = gob.Scattermapbox(lat=[y1, y2], lon=[x1, x2], mode='lines', line=dict(width=1, color='grey'), name='All rails', legendgroup='All rails')
        else:
            result = gob.Scattermapbox(lat=[y1, y2], lon=[x1, x2], mode='lines', line=dict(width=1, color='grey'), name='All rails', legendgroup='All rails', showlegend=False)
        countLegend += 1
        dataVisualise.append(result)

def connectLine(begin, end, returnPlotMap):
    """ A function for connecting two stations in a plot, specifically
        for the whole line.

        Args:
            begin: station beginning
            end: station end
            returnPlotMap: RailwayList, stationList, data

        Returns:
            y1, y2, x1, x2 (coordinates)
    """
    nameBegin = begin
    nameEnd = end
    stationList = returnPlotMap[1]
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
    return y1, y2, x1, x2

def lineConnection(maxRail, returnPlotMap):
    """ A function for plotting the assigned connections between stations (line).

        Args:
            maxRail: line with maximum score (determined by an algorithm)
            returnPlotMap: RailwayList, stationList, data
    """
    width = 2
    alreadyListed = []
    # connect rails in all trajectories
    for i in range(len(maxRail.TrajectoryList)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        label = "Trajectory " + str(i+1)
        trajColor = 'rgb(' + str(r) + ', ' + str(g) + ', ' + str(b) + ')'
        countLegend = 0
        for j in range(len(maxRail.TrajectoryList[i].Raillist)):
            if j == 0:
                y1, y2, x1, x2 = connectLine(maxRail.TrajectoryList[i].Raillist[j].stationBeginning, maxRail.TrajectoryList[i].Raillist[j].stationEnd, returnPlotMap)
            else:
                y1, y2, x1, x2 = connectLine(maxRail.TrajectoryList[i].Raillist[j].stationBeginning, maxRail.TrajectoryList[i].Raillist[j].stationEnd, returnPlotMap)

            count = 1;
            countEven = 0
            countOdd = 0
            coordinates = [y1, y2, x1, x2]
            for coordinateBlock in alreadyListed:
                if (coordinateBlock == coordinates):
                    count += 1
            alreadyListed.append(coordinates)
            coordinatesReverse = [y2, y1, x2, x1]
            alreadyListed.append(coordinatesReverse)

            if (countLegend == 0):
                legendShow = True
            else:
                legendShow = False
            if (count % 2 == 0):
                countEven += 1
                result = gob.Scattermapbox(lat=[y1, (y1+y2-0.003*countEven)/2, y2], lon=[x1, (x1+x2-0.003*countEven)/2, x2], mode='lines', line=dict(width=width, color=trajColor), name=label, legendgroup=label, showlegend=legendShow)
            else:
                countOdd += 1
                rico = -(x1-x2)/(y1-y2)
                result = gob.Scattermapbox(lat=[y1, (y1+y2+0.003*countOdd)/2, y2], lon=[x1, (x1+x2+0.003*countOdd)/2, x2], mode='lines', line=dict(width=width, color=trajColor), name=label, legendgroup=label, showlegend=legendShow)
            dataVisualise.append(result)
            countLegend += 1

def makePlot(maxRail, returnPlotMap):
    """ Shows the plot.

        Args:
            maxRail: line with maximum score (determined by an algorithm)
            returnPlotMap: RailwayList, stationList, data
    """
    data = returnPlotMap[2]
    dataVisualise.append(data)
    title = "Line with score " + str(maxRail.SLine())
    layout = gob.Layout(title=title, autosize=True, hovermode='closest', mapbox=dict(accesstoken=mapbox_access_token, bearing=0, center=dict(lat=52.4, lon=4.9), pitch=0, zoom=10), showlegend=True)
    fig = dict(data=dataVisualise, layout=layout)
    plly.offline.plot(fig, filename='visualisation/Visualisation_mapLines.html')

def printTest(maxRail):
    for i in range(len(maxRail.TrajectoryList)):
        print("")
        print("Traject {}".format(i+1))
        print("---------")
        for j in range(len(maxRail.TrajectoryList[i].Raillist)):
            print(maxRail.TrajectoryList[i].Raillist[j].stationBeginning, "trajectBeginning: ", maxRail.TrajectoryList[i].trajectBeginStation, "trajectEnd: ", maxRail.TrajectoryList[i].trajectEndStation)
            print(maxRail.TrajectoryList[i].Raillist[j].stationEnd, "trajectBeginning: ", maxRail.TrajectoryList[i].trajectBeginStation, "trajectEnd: ", maxRail.TrajectoryList[i].trajectEndStation)

def printLine(maxRail):
    """ A function for printing a line in a table.

        Args:
            maxRail: line with maximum score (determined by an algorithm).
    """
    trajectoryNames = []
    railsInTrajectories = []
    for i in range(len(maxRail.TrajectoryList)):
        name = str("Trajectory {}".format(i+1))
        trajectoryNames.append(name)
        stationsOrder = []
        stationFirst = maxRail.TrajectoryList[i].Raillist[0].stationEnd
        stationsOrder.append(stationFirst)
        lastStation = maxRail.TrajectoryList[i].Raillist[0].stationBeginning
        stationsOrder.append(lastStation)
        control = 1
        while control == 1:
            for j in range(1, len(maxRail.TrajectoryList[i].Raillist)):
                if (maxRail.TrajectoryList[i].Raillist[j].stationBeginning == lastStation and maxRail.TrajectoryList[i].Raillist[j].stationEnd != lastStation):
                    lastStation = maxRail.TrajectoryList[i].Raillist[j].stationEnd
                    stationsOrder.append(lastStation)
                    control = 0
                elif (maxRail.TrajectoryList[i].Raillist[j].stationEnd == lastStation and maxRail.TrajectoryList[i].Raillist[j].stationBeginning != lastStation):
                    lastStation = maxRail.TrajectoryList[i].Raillist[j].stationBeginning
                    stationsOrder.append(lastStation)
                    control = 0
                else:
                    stationsOrder = []
                    stationFirst = maxRail.TrajectoryList[i].Raillist[0].stationBeginning
                    stationsOrder.append(stationFirst)
                    lastStation = maxRail.TrajectoryList[i].Raillist[0].stationEnd
                    stationsOrder.append(lastStation)
        railsInTrajectories.append(stationsOrder)
    trace = gob.Table(header=dict(values=trajectoryNames, fill = dict(color='rgba(50, 50, 50, 0.1)')), cells=dict(values=railsInTrajectories))
    data = [trace]
    plly.offline.plot(data, filename = 'visualisation/Visualisation_tableLines.html')
