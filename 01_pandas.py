import pandas as pd

# data frame - rows and columns
df = pd.read_csv('/home/filip/Programming/Courses/Pandas/data/survey_results_public.csv')
schema_df = pd.read_csv('/home/filip/Programming/Courses/Pandas/data/survey_results_schema.csv')

# number of rows and columns
print(df.shape)

# info about rows and columns, also datatypes
# print(df.info())

# displaying info about schema
# pd.set_option('display.max_columns', 85)
# pd.set_option('display.max_rows', 85)
# print(schema_df)

# set pandas to display all columns
# pd.set_option('display.max_columns', 85)
# print(df)

# show a certain number of rows
print(df.head(10))
print(df.tail(10))
