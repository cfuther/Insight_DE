
import sys
import pandas as pd


# read input file
inputfile = sys.argv[1]
df = pd.read_csv(inputfile,sep=',')

# remove duplicate rows
df.drop_duplicates(inplace=True)

# check on NaNs
# If cost is NaN, does not affect results, keep. 
# If medication name is NaN, it will create a new group NaN, which does not make sense, remove.
# If last name/first name is NaN, it will affect the count results, remove.
df = df[(df.drug_name.notnull()) & (df.prescriber_last_name.notnull()) & (df.prescriber_first_name.notnull())]

# combine last name and first name to a new column
df['prescriber_name'] = df['prescriber_last_name']+(df['prescriber_first_name'])

# groupby to count unique names and sum total cost
df_count = df.groupby('drug_name').agg({'prescriber_name':'nunique','drug_cost':'sum'}).reset_index().sort_values(['drug_cost','drug_name'], ascending=[False,True])

# rename columns
df_count = df_count.rename(columns={'prescriber_name':'num_prescriber','drug_cost':'total_cost'})

# write output
outputfile = sys.argv[-1]
df_count.to_csv(outputfile,sep=',', index=False, header=True)

