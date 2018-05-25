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
            dataStations: Scattermapbox query of all stations
    """
    stationLat = []
    stationLon = []
    stationNames = []

    # for all stations: add coordinates and name to lists
    for station in stationList:
        x = float(station.y)
        y = float(station.x)
        stationLon.append(x)
        stationLat.append(y)
        stationNames.append(station.name)

    # scattermapbox query for plotting all stations with lon, lat and name
    dataStations = gob.Scattermapbox(lat=stationLat, lon=stationLon, mode='markers', marker=dict(size=7, color='red'),
                   text=stationNames, name='Stations', legendgroup='Stations')
    return RailwayList, stationList, dataStations

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

    # determine coordinates beginstation
    for i in range(len(stationList)):
        if (stationList[i].name == nameBegin):
            x1=float(stationList[i].y)
            y1=float(stationList[i].x)
            break

    # determine coordinates endstation
    for i in range(len(stationList)):
        if (stationList[i].name == nameEnd):
            x2=float(stationList[i].y)
            y2=float(stationList[i].x)
            break
    return y1, y2, x1, x2

def mapConnection(returnPlotMap):
    """ A function for plotting all railways between stations.

        Args:
            returnPlotMap: RailwayList, stationList, data
    """
    RailwayList = returnPlotMap[0]
    stationList = returnPlotMap[1]
    countLegend = 0

    # for all possible connections in the map, determine coordinates
    for connection in RailwayList:
        y1, y2, x1, x2 = connect(connection.stationBeginning, connection.stationEnd, stationList)

        # scattermapbox query for plotting connections, all in 1 legendgroup
        if (countLegend == 0):
            result = gob.Scattermapbox(lat=[y1, y2], lon=[x1, x2], mode='lines', line=dict(width=1, color='grey'),
                                       name='All rails', legendgroup='All rails')
        # only a legend for the first (no duplicates)
        else:
            result = gob.Scattermapbox(lat=[y1, y2], lon=[x1, x2], mode='lines', line=dict(width=1, color='grey'),
                                       name='All rails', legendgroup='All rails', showlegend=False)
        countLegend += 1

        # all queries in a list for later use
        dataVisualise.append(result)

def lineConnection(maxRail, returnPlotMap):
    """ A function for plotting the assigned connections between stations (line).

        Args:
            maxRail: line with maximum score (determined by an algorithm)
            returnPlotMap: RailwayList, stationList, data
    """
    stationList = returnPlotMap[1]
    alreadyListed = []

    # for all trajectories in line
    for i in range(len(maxRail.TrajectoryList)):

        # determine random color for line
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        trajColor = 'rgb(' + str(r) + ', ' + str(g) + ', ' + str(b) + ')'

        countLegend = 0
        label = "Trajectory " + str(i+1)
        for j in range(len(maxRail.TrajectoryList[i].Raillist)):
            y1, y2, x1, x2 = connect(maxRail.TrajectoryList[i].Raillist[j].stationBeginning,
                                     maxRail.TrajectoryList[i].Raillist[j].stationEnd, stationList)
            coordinates = [y1, y2, x1, x2]

            # check if rail is used multiple times
            countEven = 1
            countOdd = 2
            count = 1
            for coordinateBlock in alreadyListed:
                if (coordinateBlock == coordinates):
                    count += 1
                    if (count % 2 == 0):
                        countEven += 1
                    else:
                        countOdd += 1

            alreadyListed.append(coordinates)
            coordinatesReverse = [y2, y1, x2, x1]
            alreadyListed.append(coordinatesReverse)

            if (countLegend == 0):
                legendShow = True
            else:
                legendShow = False

            # if count even, scattermapbox query for plotting rail, extra curve
            if (count % 2 == 0):
                result = gob.Scattermapbox(lat=[y1, (y1+y2-0.001*countEven)/2, y2], lon=[x1, (x1+x2-0.001*countEven)/2, x2], mode='lines',
                                           line=dict(width=2, color=trajColor), name=label, legendgroup=label, showlegend=legendShow)

           # if count odd, scattermapbox query for plotting, extra curve other side
            else:
                result = gob.Scattermapbox(lat=[y1, (y1+y2+0.001*countOdd)/2, y2], lon=[x1, (x1+x2+0.001*countOdd)/2, x2], mode='lines',
                                           line=dict(width=2, color=trajColor), name=label, legendgroup=label, showlegend=legendShow)

           # put query in list for later use
            dataVisualise.append(result)
            countLegend += 1

def makePlot(maxRail, returnPlotMap):
    """ Shows the plot.

        Args:
            maxRail: line with maximum score (determined by an algorithm)
            returnPlotMap: RailwayList, stationList, data
    """
    # add plotting stations query to list
    dataStations = returnPlotMap[2]
    dataVisualise.append(dataStations)

    # make plot (map) for all data accumulated
    title = "Line with score " + str(round(maxRail.SLine(), 1))
    layout = gob.Layout(title=title, autosize=True, hovermode='closest', mapbox=dict(accesstoken=mapbox_access_token,
                        bearing=0, center=dict(lat=52.4, lon=4.9), pitch=0, zoom=10), showlegend=True)
    fig = dict(data=dataVisualise, layout=layout)
    plly.offline.plot(fig, filename='visualisation/Visualisation_mapLines.html')

def printTest(maxRail):
    for i in range(len(maxRail.TrajectoryList)):
        print("")
        print("Traject {}".format(i+1))
        print("---------")
        for j in range(len(maxRail.TrajectoryList[i].Raillist)):
            print(maxRail.TrajectoryList[i].Raillist[j].stationBeginning, "trajectBeginning: ",
                  maxRail.TrajectoryList[i].trajectBeginStation, "trajectEnd: ", maxRail.TrajectoryList[i].trajectEndStation)
            print(maxRail.TrajectoryList[i].Raillist[j].stationEnd, "trajectBeginning: ",
                  maxRail.TrajectoryList[i].trajectBeginStation, "trajectEnd: ", maxRail.TrajectoryList[i].trajectEndStation)

def printLine(maxRail):
    """ Prints a line in a table. Columns: trajectories.

        Args:
            maxRail: line with maximum score (determined by an algorithm).
    """
    trajectoryNames = []
    railsInTrajectories = []

    # for all trajectories in line
    for i in range(len(maxRail.TrajectoryList)):

        # make list of names Trajectory 1, Trajectory 2, etc.
        name = str("Trajectory {}".format(i+1))
        trajectoryNames.append(name)

        # make list for stationOrder, append all endstations and beginstation for first
        stationsOrder = []
        for j in range(0, len(maxRail.TrajectoryList[i].Raillist)):
            if (j == 0):
                stationFirst = maxRail.TrajectoryList[i].Raillist[0].stationBeginning
                stationsOrder.append(stationFirst)
            lastStation = maxRail.TrajectoryList[i].Raillist[j].stationEnd
            stationsOrder.append(lastStation)

        # add to list of rails in trajectories
        railsInTrajectories.append(stationsOrder)

    # plot all data in table (header is names, cells are rails)
    data = [gob.Table(header=dict(values=trajectoryNames, fill = dict(color='rgba(50, 50, 50, 0.1)')),
            cells=dict(values=railsInTrajectories))]
    plly.offline.plot(data, filename = 'visualisation/Visualisation_tableLines.html')
