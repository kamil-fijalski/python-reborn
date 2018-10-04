# Loading data
import pandas as pd

xlsx_path = 'test.xlsx'
df = pd.read_excel(xlsx_path)  # df -> dataframe
# print(df)

y = df.keys()
print(y)

# creating single dataframe (here: with phone numbers)
z = df[['phone']]
print(z)

a1 = df['postal'].unique()  # find unique elements in df
print(a1)
print("Length of A1: " + str(len(a1)))

a2 = df['ccnumber'] >= 4903431815520553
print(a2)  # list of boolean values

# new dataframe with condition
a3 = df[df['ccnumber'] >= 4903431815520553]
print("Length of A3: " + str(len(a3)))
print(a3)
a3.to_csv('test_csv.csv')
