# TeamThomasDeTrein

**Contributors:** Mark van den Hoven, Thymen van de Lagemaat and Teunis van der Hofstad

Assignment for the UvA-course **'Heuristics'**

**Case:** [RailNL](http://heuristieken.nl/wiki/index.php?title=RailNL)

## Summary

This project is made for determining what (existing) rails can best be used for connecting train stations in a certain area. A distinction can be made between ordinary railways and critical railways, that are logistically most important. 

The project is focused on determining the best line for trains in The Netherlands or the provinces Noord- and Zuid-Holland. 

Determining what trajectories can best be made is done by maximizing the following **formula:** 

	S = p*10.000 - (t*20 + min/10). 
		
	S is the score, p is the fraction of critical railways used, t is the number of trajectories used and min is the total amount of time (in minutes) of all the trajectories combined.  

## Files

The repository contains several **files:** 

	main.py: The main function of the program, triggering all other files. 
	
	.gitignore: File to be ignored by gitHub. 
	
	README.md: (This) file describing the project and how to use it. 
	
	requirements.txt: A file stating what extra plugins (and what versions) are needed to install to run the program. 
	
	(FOLDER) algorithms:
	
		- hillClimber.py: Contains the hillClimber() function. This changes, adds and removes trajectories from a line as long as the score improves. 

		- randomAlgorithm.py: Contains several functions for determining a random line. The number of trajectories is chosen randomly, as well as the rails in all trajectories. 

		- SimulatedAnnealing.py: Contains functions for adjusting a line. Starts with a line and changes the line according to makeSnakeTrajectory() or the random algorithm. Accepts changes when the score becomes lower only if the temperature is high enough. 
	
	(FOLDER) classes:
	
		- helpers.py: A supporting file. For now containing a program that displays all railways and their information to make things visible for programmers. 

		- lineClass.py: A class containing all information about a line, including the TrajectoryList, RailwayList, criticalRailwayList and inverseDict. It also contains several functions for a line. 

		- railAndStationClass.py: A file containing two classes: Rail and Station. Rail is a class for a rail between stations, Station for the stations themselves. 

		- trajectoryClass.py: A file containing the Trajectory class. This includes a list of railways used and a list of all railways, but several functions as well. 
	
	(FOLDER) data:
	
		- ConnectiesHolland.csv: A file containing all railways (for intercity-trains) in the provinces of Noord- and Zuid-Holland (The Netherlands).

		- StationsHolland.csv: A file containing all stations (for intercity-trains) in the provinces of Noord- and Zuid-Holland (The Netherlands). 

		- StationsHollandCritical.csv: A file containing all stations (for intercity-trains) in the provinces of Noord- and Zuid-Holland (The Netherlands). All stations are critical stations. 

		- ConnectiesNationaal.csv: A file containing all railways (for intercity-trains) in The Netherlands. 

		- StationsNationaal.csv: A file containing all stations (for intercity-trains) in The Netherlands. 

		- StationsNationaalCritical.csv: A file containing all stations in The Netherlands. All stations are critical stations. 
	
	(FOLDER) experimentation:
	
		- README.md: A short summary of reasearch done with the program. 
	
	(FOLDER) visualisation:
	
		- visualisation.py: A file containing functions for making a map visualisation and a table visualisation of a line. 

		- Visualisation_mapLines.html: A file containg the map visualisation of a line. Updated every time visualize() is used. 

		- Visualisation_tableLines.html: A file containg the table visualisation of a line. Updated every time printLine() is used.

## Use

To make use of the project you have to follow the following steps in main.py:

	Step 1: Select the file you want to use: 'nationaal' for the map of The Netherlands or 'holland' for the map of the provinces Noord- and Zuid-Holland. 
	
	Step 2: Select the critical station file you want to use: 'normal' for the number determined by the case or 'critical' for making all stations critical. 
	
	Step 3: Select the line (different for each algorithm) you want to use: randomLine, hillclimberLine or simulatedannealingLine. Make sure you comment out the other two lines you don't want to use (saves computing power).
	
	Step 4: Change the parameters for the line used.
	
		For randomLine: 
			line (Line): A Line element which you want to update.
			amountOfTrajectories (int): Amount of trajectories which you want to add.
			iterarations (int): Amount of rails you want to add
			amountOfRails (int): Amount of rails you want to add per trajectory
			
		For hillclimberLine:
			line (Line): Line element which you want to improve
			iterations (int): Amount of iterations which you want to use
			replace (string): Input "random" when you want to replace for random trajectories, Input "snake" when you want to replace for snake trajectories
			amountOfRails (int): Amount of rails you want to add per trajectory
			
		For simulatedAnnealingLine:
		        line (Line): A Line element which you want to update.
			amountOfTrajectories (int): Amount of trajectories which you want to add
			stepSize (int): Amount of steps you want to take to make the trajectory
			iterations (int): Amount of times you want to try to improve all the the trajectories
			replace (string): Input "random" when you want to update trajectories with random algorithm and "snake" for the makeSnakeTrajectory function
			multiplicationAdd (float): Multiplication factor of T for adding rails
			multiplicationChop (float): Multiplication factor of T for chopping rails
			
	Step 5: Change setMultiplicationAdd() and setMultiplicationChop() when you have chosen to use "snake". This will determine the temperature used in the simulated annealing process. 
	
	Step 6: Set the line you want to visualise to randomLine, hillclimberLine or simulatedAnnealingLine. 

All files are free to use. For **questions** you can always send an email to markvandenhoven@icloud.com, thymenyj@gmail.com, teunisvanderhofstad@hotmail.com. 
