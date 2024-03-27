# champions_league_draw_probability
Champions League Round of 16 Draw Probability Calculation
This Python script calculates the probabilities for teams facing each other in the UEFA Champions League Round of 16 draw. The probabilities are calculated using a Monte Carlo simulation approach, considering constraints where teams from the same group or country cannot face each other.

# Dependencies
The script utilizes several Python libraries:

'pandas': For data manipulation, particularly for handling the team data stored in an Excel file.
'numpy': For numerical operations, primarily to create and manipulate arrays for probability calculations.
'random': For shuffling the teams during the simulation.
'csv': For writing the probability table to a CSV file.

# Team Class
The Team class represents a team participating in the Champions League. It has attributes like name, country, and a unique number identifier.

# Probability Calculation
The prob_calc function calculates the probability of teams facing each other in the draw. It follows these steps:

Shuffle the list of teams to randomize the draw.
Check if any teams violate the constraints (teams from the same group or country facing each other). If so, return a probability of 0.
Increment a global counter to keep track of simulation iterations.
Update the probability table based on the draw results.
Initialization and Data Loading
The script loads team data from an Excel file named teams.xlsx.
It separates the teams into two sets (seed1 and seed2) to simulate the draw process.
Simulation
The simulation (while loop) runs until a specified number of iterations (100000 in this case). During each iteration, the prob_calc function is called to simulate a draw.

# Probability Table
Once the simulation is complete, the script normalizes the probability table and prints it. The probability table represents the likelihood of each team facing another team in the Round of 16 draw.

# Writing to CSV
Finally, the probability table is written to a CSV file named prob_table.csv for further analysis or visualization.

# Conclusion
This script provides a systematic approach to estimate the probabilities of various draw scenarios for the UEFA Champions League Round of 16, incorporating constraints based on team groups and countries.
