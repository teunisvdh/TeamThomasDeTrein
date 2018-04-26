def printList(railwayList):
    """Prints list indexed list of all railway connections.

        Args:
            RailwayList (list): List of railways that you want to print.

        Returns:
            Printed list of indexed railways.
    """
    for i in range(len(railwayList)):
        print('{}:{},{},{}'.format(i, railwayList[i].stationBeginning,
            railwayList[i].stationEnd,
            railwayList[i].minutes))
