import csv, sys, os, random
import matplotlib.pyplot as plt
import matplotlib.lines as lin
import plotly as plly
import plotly.graph_objs as gob
sys.path.append('C:/TeamThomasDeTrein/classes')
sys.path.append('C:/TeamThomasDeTrein/algorithms')
from algorithms import randomAlgorithm
from matplotlib.widgets import CheckButtons

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
    """
    # plot all stations
    stationLat = []
    stationLon = []
    stationNames = []
    for station in stationList:
        x = float(station.y)
        y = float(station.x)
        plot = plt.plot(x, y, 'ro-')
        # name = station.name
        stationLon.append(x)
        stationLat.append(y)
        stationNames.append(station.name)
        names = plt.annotate(station.name, xy=(x,y))
    data = gob.Scattermapbox(lat=stationLat, lon=stationLon, mode='markers', marker=dict(size=7, color='red'), text=stationNames, name='Stations', legendgroup='Stations')

    return RailwayList, stationList, data

def connect(begin, end, stationList):
    """ A function for connecting two stations in a plot.

        Args:
            begin = station beginning, end = station end
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
    plt.plot([x1, x2], [y1, y2], 'gray', linewidth=0.2)

    return y1, y2, x1, x2

# plot all connections
def mapConnection(returnPlotMap):
    """ A function for plotting all railways between stations.

        Args:
            returnPlotMap: RailwayList, stationList.
    """
    mapLat = []
    mapLon = []
    data = []
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
    distance = random.uniform(0, 0.0000)
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
    return y1, y2, x1, x2

def lineConnection(maxRail, returnPlotMap):
    """ A function for plotting the assigned connections between stations (line).

        Args:
            maxRail: line with maximum score (determined by an algorithm).
            returnPlotMap: RailwayList, stationList.
    """
    colors = ['r', 'g', 'c', 'm', 'y', 'b', 'k']
    styles = [':', '-.', '--']
    lineStyle = []
    alreadyListed = []
    for color in colors:
        for style in styles:
            thisStyle = color + style
            lineStyle.append(thisStyle)

    # mapColors = ['blue', 'black', 'orange', 'green', 'purple', 'brown', 'pink', 'yellow', 'rgb(50, 50, 50)', 'rgb(0, 50, 50)', 'rgb(50, 0, 50)', 'rgb(50, 50, 0)', 'rgb(50, 20, 200)', 'rgb(50, 20, 200)', 'rgb(50, 20, 200)', 'rgb(50, 20, 200)', 'rgb(50, 20, 200)', 'rgb(50, 20, 200)', 'rgb(50, 20, 200)']
    mapStyles = ['dash', 'dot', 'dashdot']
    width = 2
    # connect rails in all trajectories
    for i in range(len(maxRail.TrajectoryList)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        style = random.choice(lineStyle)
        lineStyle.remove(style)
        label = "Trajectory " + str(i+1)
        # trajColor = random.choice(mapColors)
        trajColor = 'rgb(' + str(r) + ', ' + str(g) + ', ' + str(b) + ')'
        # mapColors.remove(trajColor)
        trajStyle = random.choice(mapStyles)
        countLegend = 0
        for j in range(len(maxRail.TrajectoryList[i].Raillist)):
            if j == 0:
                y1, y2, x1, x2 = connectLine(maxRail.TrajectoryList[i].Raillist[j].stationBeginning, maxRail.TrajectoryList[i].Raillist[j].stationEnd, returnPlotMap, style, label)
            else:
                y1, y2, x1, x2 = connectLine(maxRail.TrajectoryList[i].Raillist[j].stationBeginning, maxRail.TrajectoryList[i].Raillist[j].stationEnd, returnPlotMap, style, '')

            count = 0;
            coordinates = [y1, y2, x1, x2]
            alreadyListed.append(coordinates)
            coordinatesReverse = [y2, y1, x2, x1]
            alreadyListed.append(coordinatesReverse)
            for coordinateBlock in alreadyListed:
                if (coordinateBlock == coordinates):
                    count += 1

            if (countLegend == 0):
                result = gob.Scattermapbox(lat=[y1, y2], lon=[x1, x2], mode='lines', line=dict(width=width, color=trajColor), name=label, legendgroup=label, showlegend=True)
            else:
                result = gob.Scattermapbox(lat=[y1, y2], lon=[x1, x2], mode='lines', line=dict(width=width, color=trajColor), name=label, legendgroup=label, showlegend=False)
            dataVisualise.append(result)
            countLegend += 1

def makePlot(maxRail, returnPlotMap):
    """ Shows the plot.
    """
    # make plot
    data = returnPlotMap[2]
    dataVisualise.append(data)
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.title("Line with score " + str(maxRail.SLine()), ha='center')
    plt.axis('equal')
    plt.legend()
    title = "Line with score " + str(maxRail.SLine())
    layout = gob.Layout(title=title, autosize=True, hovermode='closest', mapbox=dict(accesstoken=mapbox_access_token, bearing=0, center=dict(lat=52.5, lon=4.5), pitch=0, zoom=10), showlegend=True)
    fig = dict(data=dataVisualise, layout=layout)
    plly.offline.plot(fig, filename='Visualisation_mapLines.html')
    plt.show()

def printLine(maxRail):
    """ A function for printing a line.

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
    plly.offline.plot(data, filename = 'Visualisation_tableLines.html')
