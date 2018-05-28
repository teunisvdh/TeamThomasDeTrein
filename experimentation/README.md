Team Thomas (de trein) 
Summary of the experimentation of case RailNL

Introduction
In our research we have used three different algorithms: 
-      Random algorithm
-      Hillclimber algorithm
-      Simulated Annealing algorithm
 
Our goal is to determine the pros and cons of using these algorithms in this specific case (RailNL). We will answer the following sub questions: 
What is the impact of the following actions on the quality (final and average score) of the algorithms? 
-      Changing the map (from Holland to Nationaal);
-      Changing the number of critical stations;
-      Changing the parameters used in the algorithm;
 

- Subquestion 1: How much effect does a change in the map have on the quality of the algorithms? 
 
To answer this question, the three algorithms used in this case will be researched.

Two maps are used to run the algorithms, Holland and Nationaal. The map of Holland contains 28 stations, whereof seven so called critical stations. Nationaal contains 61 station, whereof 23 critical stations. 

The three algorithms will be run a different amount of times depending on how much time the algorithm needs to come to a solution. De highest and average scores will be compared, based on the type of map and algorithm.  
 
Random algorithm: 
The following parameters were used: 
Times algorithm runned: 500.000 (Holland) / 250.000 (Nationaal) 

Hillclimber algorithm:
The following parameters were used:

	with random:

	with snake:


Simulated Annealing algorithm:
The following parameters were used:
 
	with random:

	with snake: 



Results:

De Hillclimber-tabel laat zien dat de hoogste en gemiddelde scores van Holland hoger zijn dan de scores van Nationaal. Het lijkt erop dat een graaf met minder stations makkelijker is. 

Daarnaast is het verschil tussen de hoogste score en de gemiddelde score bij Nationaal groter dan bij Holland. Een mogelijke verklaring is dat er meerdere opties zijn bij Nationaal.




 

- Subquestion 2: How much impact does the amount of critical stations have on the quality of the algorithms?

To answer the second question, the two maps, Holland and Nationaal, are used. For each map, two graphs are created. One graph contains the original amount critical stations and the other graph is a situation where all stations are set to critical, so there are 4 scenario’s intotal.

Several parameters will be adjusted during the experimentation. The algorithms that will be 
researched are the Hillclimber and Simulated Annealing algorithms. For the Hillclimber the number of iterations can be adjusted, a well as the number of trajectories. This holds true for the Simulated Annealing algorithm too. However, two other parameters that can be changed for this algorithm are the number of snake adjustments and the temperature function. 

Random algorithm: 
The following parameters were used: 
Times algorithm runned: 500.000 (Holland) / 250.000 (Nationaal) 


Hillclimber algorithm:
The following parameters were used:

  with random:

	with snake:


Simulated Annealing algorithm:
The following parameters were used: 

  with random:

  with snake: 


 - Subquestion 3: What is the effect on the quality of the algorithms when the parameters will be adjusted over time. 
