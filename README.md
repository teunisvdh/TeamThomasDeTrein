# TeamThomasDeTrein

**Contributors:** Mark van den Hoven, Thymen van de Lagemaat and Teunis van der Hofstad

Assignment for the UvA-course **'Heuristics'**

**Case:** [RailNL](http://heuristieken.nl/wiki/index.php?title=RailNL)



This project is made for determining what (existing) rails can best be used for connecting train stations in a certain area. A distinction can be made between ordinary railways and critical railways, that are logistically most important. 

Determining what trajectories can best be made is done by maximizing the following **formula:** 

	S = p*10.000 - (t*20 + min/10). 
		
	S is the score, p is the fraction of critical railways used, t is the number of trajectories used and min is the total amount of time (in minutes) of all the trajectories combined.  

The repository contains several **files:** 

	- main.py: The main function of the program, triggering all other files. 
	
	- .gitignore: File to be ignored by gitHub. 
	
	- README.md: (This) file describing the project and how to use it. 
	
	- requirements.txt: A file stating what extra plugins (and what versions) are needed to install to run the program. 
	
	**algorithms**
	
	- hillClimber.py: Contains the hillClimber() function. This changes, adds and removes trajectories from a line as long as the score improves. 
	
	- randomAlgorithm.py: Contains several functions for determining a random line. The number of trajectories is chosen randomly, as well as the rails in all trajectories. 
	
	- SimulatedAnnealing.py: Contains functions for adjusting a line. Starts with a line and changes the line according to makeSnakeTrajectory() or the random algorithm. Accepts changes when the score becomes lower only if the temperature is high enough. 
	
	**classes**
	
	- helpers.py: A supporting file. For now containing a program that displays all railways and their information to make things visible for programmers. 
	
	- lineClass.py: A class containing all information about a line, including the TrajectoryList, RailwayList, criticalRailwayList and inverseDict. It also contains several functions for a line. 
	
	- railAndStationClass.py: A file containing two classes: Rail and Station. Rail is a class for a rail between stations, Station for the stations themselves. 
	
	- trajectoryClass.py: A file containing the Trajectory class. This includes a list of railways used and a list of all railways, but several functions as well. 
	
	**data**
	
	- ConnectiesHolland.csv: A file containing all railways (for intercity-trains) in the provinces of Noord- and Zuid-Holland (The Netherlands).
	
	- StationsHolland.csv: A file containing all stations (for intercity-trains) in the provinces of Noord- and Zuid-Holland (The Netherlands). 
	
	- StationsHollandCritical.csv: A file containing all stations (for intercity-trains) in the provinces of Noord- and Zuid-Holland (The Netherlands). All stations are critical stations. 
	
	- ConnectiesNationaal.csv: A file containing all railways (for intercity-trains) in The Netherlands. 
	
	- StationsNationaal.csv: A file containing all stations (for intercity-trains) in The Netherlands. 
	
	- StationsNationaalCritical.csv: A file containing all stations in The Netherlands. All stations are critical stations. 
	
	**experimentation**
	
	- README.md: A short summary of reasearch done with the program. 
	
	**visualisation**
	
	- visualisation.py: A file containing functions for making a map visualisation and a table visualisation of a line. 
	
	- Visualisation_mapLines.html: A file containg the map visualisation of a line. Updated every time visualize() is used. 
	
	- Visualisation_tableLines.html: A file containg the table visualisation of a line. Updated every time printLine() is used.
	
All files are free to use. For **questions** you can always send an email to markvandenhoven@icloud.com, thymenyj@gmail.com, teunisvanderhofstad@hotmail.com. 
