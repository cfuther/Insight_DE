# Insight_DE
This project was written for the code challenge of Insight Data Engineering program. The code challenge asked to generate a list of 
all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in 
descending order based on the total drug cost and if there is a tie, drug name in ascending order. 

The code /src/Pharmacy_analysis.py was written in Python 3, tested using the test input and was able to generate the desired output on both 
IPython and Anaconda Prompt platforms. Pandas was used to handle the data since it is an efficient tool to process large scale relational data.
Groupby was applied to perform aggregation for multiple variants. Self-defined test-2 includes cases with duplicate rows, same prescriber order the same drug for multiple times, NaN at different columns. Code passed both test-1 and test-2.

Passed the test at the website provided and got 4 out of 4 correct. 
