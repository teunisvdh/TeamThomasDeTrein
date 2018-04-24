import csv
import sys
import os
from data import *
from classes import classes
from classes import opendata
from classes import helpers

def main():
    with open('data/StationsHolland.csv') as csvfile:
        stationsinfo = csv.reader(csvfile, delimiter=',')
        stationLijst = []
        kritiekeStationLijst = []
        for station in stationsinfo:
            stationLijst.append(classes.Station(station[0], station[1], station[2], station[3]))
            if station[-1] == 'Kritiek':
                kritiekeStationLijst.append(station[0])

    with open('data/ConnectiesHolland.csv') as csvfile:
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

    spoorlist_1 = [sporenLijst[1], sporenLijst[0], sporenLijst[27], sporenLijst[25], sporenLijst[10]]
    traject_1 = classes.Traject(spoorlist_1)

    spoorlist_2 = [sporenLijst[3], sporenLijst[4], sporenLijst[5], sporenLijst[17]]
    traject_2 = classes.Traject(spoorlist_2)

    spoorlist_3 = [sporenLijst[12], sporenLijst[21], sporenLijst[23]]
    traject_3 = classes.Traject(spoorlist_3)

    spoorlist_4 = [sporenLijst[15], sporenLijst[19], sporenLijst[13]]
    traject_4 = classes.Traject(spoorlist_4)

    spoorlist_5 = [sporenLijst[16], sporenLijst[26], sporenLijst[27]]
    traject_5 = classes.Traject(spoorlist_5)

    spoorlist_6 = [sporenLijst[14], sporenLijst[22], sporenLijst[24], sporenLijst[11]]
    traject_6 = classes.Traject(spoorlist_6)

    spoorlist_7 = [sporenLijst[6]]
    traject_7 = classes.Traject(spoorlist_7)

    lijn_1 = [traject_1, traject_2, traject_3, traject_4, traject_5, traject_6, traject_7]

    print(classes.Lijnvoering(lijn_1, kritiekeSporenLijst).SLijnvoering())


if __name__ == "__main__":
    main()
