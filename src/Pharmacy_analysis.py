
import sys
import pandas as pd


# read input file
inputfile = sys.argv[1]
df = pd.read_csv(inputfile,sep=',')

# combine last name and first name to a new column
df['prescriber_name'] = df['prescriber_last_name']+(df['prescriber_first_name'])

# groupby to count unique names and sum total cost
df_count = df.groupby('drug_name').agg({'prescriber_name':'nunique','drug_cost':'sum'}).reset_index().sort_values(['drug_cost','drug_name'], ascending=[False,True])

# rename columns
df_count = df_count.rename(columns={'prescriber_name':'num_prescriber','drug_cost':'total_cost'})

# write output
outputfile = sys.argv[-1]
df_count.to_csv(outputfile,sep=',', index=False, header=True)

