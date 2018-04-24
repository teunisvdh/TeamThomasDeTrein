import csv
from classes import classes

def openStations(str):
    with open(str) as csvfile:
        stationsinfo = csv.reader(csvfile, delimiter=',')
        stationLijst = []
        kritiekeStationLijst = []
        for station in stationsinfo:
            print(station)
            stationLijst.append(classes.Station(station[0], station[1], station[2], station[3]))
            if station[-1] == 'Kritiek':
                kritiekeStationLijst.append(station[0])
        return kritiekeStationLijst

def openConnecties(str, kritiekeStationLijst):
    with open(str) as csvfile:
        stationsverbindingen = csv.reader(csvfile, delimiter=',')
        sporenLijst = []
        kritiekeSporenLijst = []
        for lijn in stationsverbindingen:
            sporenLijst.append(classes.Spoor(lijn[0], lijn[1], lijn[2]))
        for lijn in sporenLijst:
            if (lijn.stationBegin in kritiekeStationLijst
                or lijn.stationEind in kritiekeStationLijst
                and lijn not in kritiekeSporenLijst):
                    kritiekeSporenLijst.append(lijn)
        return sporenLijst
