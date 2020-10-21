# InsightDataChallenge2020-MySolutionInPython

This is the Python code for my solution to the insight coding challenge 2020-population rollup. Please find the relevant information in the following sections.

# How to run ? 

After cloning the repository to your local. Make sure to do some chmod magic on the shell script you want to run (e.g. chmod 777 run.sh). 

After that just execute: ./run.sh 

For running the unit tests: cd src/ && ./run_tests.sh (Optional)

# Problem definition

We were given the 2000 to 2010 Census Tract Population Change data set in excel and csv form.

We were asked to write a solution that for each Core Based Statistical Area, would find the 
* total number of census tracts, 
* total population in 2000, 
* total population in 2010 and 
* average population percent change for census tracts in this Core Based Statistical Area

With restrictions on the packages we could use (e.g. no pandas in Python) and we were asked to use only the data structures that came with the languages. 

# Structure of the repository and approach for the solution

Programming basics:

Clean code - I tried to write my code as concise and modular as possible.

Scalablity - Both reading and writing is done on a line by line basis and without allocating the memory for the full input or output file. (I tested this with a number of input lines up to 1.6 million lines)

Next section has more about these practices.

Here is how the repo/solution is structured:

- app.py runs the whole process and measures the runtime. 

- constants.py has the constants like the names of input/output files and column numbers and names that comes with the census data.

- We have two entities (/src/Entities): One of them is the summary we keep (AreaPopulationChangeSummary.py) of the whole input and the other one is a single data record of the population change in the input file as a class of its own (PopulationChangeDatum.py).

- Input/Output (IO) operations are done in respective classes in the "/src/IO" directory.

- TractPopulationChangeProcessor.py is where the data cleaning/selection process happens.

- Once we read the input, we process each line in a csv (/src/processing) and we keep a dictionary of area codes and validate the type of the columns (TractPopulationChangeProcessor.py). We summarize them after each datum is processed (TractPopulationChangeSummerizer.py).

- We write the summary to the report.csv.

# Some of the design decisions explained

- (X)'s

I considered these values that were on some cells, values to be ignored or NULL.

- Numbers in quotes (e.g. "3,457.50")

I handle the numbers in quotes differently as they would raise an exception with a isnumeric() style filter. See the TractPopulationChangeProcessor.py class for this. 

- Missing values in tract title 

As long as we have a valid value for Core Based Statistical Area, this code should behave as expected (explained above). If the input is missing titles but has area codes, the program looks for the title that maches the area code and still calculates the summaries. 

- Rounding up the 0.001% and 0.005% intervals (requirement in the challange)

I use the round method in Python (format(round(decimal_value, 2)).rstrip('0').rstrip('0').rstrip('.')) which is validated by hand using a scientific round website.

# Bonus 

I wrote this exact code snippet and tests in C#. Just for fun you can check that out too ! Here is the link (that repo will be public after the deadline) :
https://github.com/yigitk/InsightCodingChallange2020-DotnetCoreCsharp

