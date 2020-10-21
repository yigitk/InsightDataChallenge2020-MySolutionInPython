# InsightDataChallenge2020-MySolutionInPython

This is the Python code for my solution to the insight coding challenge 2020-population rollup. Please find the relevant information in the following sections.

# How to run ? 

After cloning the repository to your local. Make sure to do some chmod magic on the shell script you want to run (e.g. chmod 777 run.sh). 

After that just execute: ./run.sh 

For running the unit tests: cd src/ && ./run_tests.sh (Optional)

#Problem definition

We were given the 2000 to 2010 Census Tract Population Change data set in excel and csv form.

We were asked to write a solution that for each Core Based Statistical Area, would find the 
* total number of census tracts, 
* total population in 2000, 
* total population in 2010 and 
* average population percent change for census tracts in this Core Based Statistical Area

With restrictions on the packages we could use (e.g. no pandas in Python) and we were asked to use only the datastructures that came with the languages. 

# Structure of the repository and approach for the solution

Programming basics:

Clean code - I tried to write my code with as short and as modular I could.

Scalablity - Both reading and writing is done on a line by line basis and without allocating the memory for the full input or output file. (I tested this with a number of input lines up to 1.6 million lines)

Next section has more about these practices.

Here is how the repo/solution is structured:

- app.py runs the whole process and keeps the runtime. 

- constants.py has the constants like the input/output files and column numbers and names that comes with the census data.

- We have two entities(/src/Entities): One of them is the summary we keep (AreaPopulationChangeSummary.py) of the whole input and other one is a single data record in the population change in the input file as a class of its own(PopulationChangeDatum.py).

- Input/Output (IO) operations are done in respective classes in the "/src/IO" directory.

- Once we read the input, we process (/src/processing) each line in a csv and we keep a dictionary of area codes and validate the type of the columns (TractPopulationChangeProcessor.py) and we summarize them after each datum is processed (TractPopulationChangeSummerizer.py).

- TractPopulationChangeProcessor.py is where the data cleaning/selection process happens.

- We write the summary to the report.csv.

# Some of the design decisions

- (X)'s

I handled these on some cells as values to ignore or NULL.

- Numbers in quotes

I handle the numbers in quotes differently as they would raise an exception with a isnumeric() style filter. See the Processing classes for this. 

- Missing values in tract title 

As long as we have a valid value for Core Based Statistical Area, this code should do what it is asked (explained above). If we are missing some titles it looks for the title that maches the number and still calculates the summaries. 

- Missing values in Core Based Statistical Area

Can't do anything about this hence we ignore thoese rows

- Rounding up the 0.001% and 0.005% intervals (requirement in the challange)

I use the round method in Python which I validated from a scientific rounder from Google.

