Team Thomas (de trein) 
Summary of the experimentation of case RailNL

Introduction:

	In our research we have used three different algorithms: 
		- Random algorithm
		- Hillclimber algorithm
		- Simulated Annealing algorithm

	Our goal is to determine the pros and cons of using these algorithms in this specific case (RailNL). We will answer the 		following sub questions: 
	What is the impact of the following actions on the quality (final and average score) of the algorithms? 
		- Changing the map (from Holland to Nationaal);
		- Changing the number of critical stations;
		- Changing the parameters used in the algorithm;


	Random algorithm: 
	The following parameters were used: 
	Times algorithm runned: 500.000 (Holland) / 250.000 (Nationaal) 

	Hillclimber algorithm (random and snake):
	The following parameters were used:
		iterations: 10
		stepSize: 10
		amountOfRails: 10

	Simulated Annealing algorithm (random and snake), testing temerature:
	The following parameters were used:
		iterations: 10
		stepSize: 15
		amountOfRails: 10
		temperature: variable (tested)

	Simulated Annealing algorithm (random and snake), testing iterations and stepSize:
	The following parameters were used:
		iterations: variable (tested)
		stepSize: variable (tested)
		amountOfRails: 10
		temperature: 10 for add, 100 for chop
	
Results:

	Holland vs Nationaal (random):

	Holland:
		- critical: random vs snake (hillclimber)
		![graph](https://github.com/teunisvdh/TeamThomasDeTrein/blob/master/experimentation/doc/Holland%20critical%20vs%20not%20critical%2C%20random%20vs%20snake%20(9000%2B).png)
		- not critical: random vs snake (hillclimber) 

	Nationaal:
		- critical: random vs snake (hillclimber)
		- not critical: random vs snake (hillclimber) 


	Holland: 
	Simulated Annealing snake: 
		- temperature 5 add/ 50 chop
		- temperature 10 add/ 100 chop
		- temperature 20 add/ 200 chop
		
	Nationaal: 
	Simulated Annealing snake: 
		- temperature 5 add/ 50 chop
		- temperature 10 add/ 100 chop
		- temperature 20 add/ 200 chop 
		
	Nationaal:
	Simulated Annealing snake:
		- 5 iterations/ 5 stepSize
		- 5 iterations/ 10 stepSize
		- 5 iterations/ 20 stepSize
		- 10 iterations/ 5 stepSize
		- 20 iterations/ 5 stepSize
		- 10 iterations/ 20 stepSize
		- 10 iterations/ 20 stepSize		
		- 20 iterations/ 20 stepSize

Conclusion:

	
	
