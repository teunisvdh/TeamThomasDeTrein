# TeamThomasDeTrein

**Contributors:** Mark van den Hoven, Thymen van de Lagemaat and Teunis van der Hofstad

Assignment for the UvA-course **'Heuristics'**

**Case:** [RailNL](http://heuristieken.nl/wiki/index.php?title=RailNL)



This project is made for determining what (existing) rails can best be used for connecting train stations in a certain area. A distinction can be made between ordinary railways and critical railways, that are logistically most important. 

Determining what trajectories can best be made is done by maximizing the following **formula**: 

	S = p*10.000 - (t*20 + min/10). 
		
	S is the score, p is the fraction of critical railways used, t is the number of trajectories used and min is the total amount of time (in minutes) of all the trajectories combined.  

The repository contains several **files**: 

	- main.py: The main function of the program, triggering all other files. 
	
	- classes.py: Multiple classes and functions used in the program.  
	
	- helpers.py: A supporting file. For now containing a program that displays all railways and their information to make things visible for programmers. 
	
	- ConnectiesHolland.csv: A file containing all railways (for intercity-trains) in the provinces of Noord- and Zuid-Holland (The Netherlands).
	
	- StationsHolland.csv: A file containing all stations (for intercity-trains) in the provinces of Noord- and Zuid-Holland (The Netherlands). 

All files are free to use. For **questions** you can always send an email to markvandenhoven@icloud.com, thymenyj@gmail.com, teunisvanderhofstad@hotmail.com. 
