"""Example for using Pandas on an XLS as a Python Script"""
import pandas as pd

df = pd.read_excel("sheet_1_with_simple_logic.xls")
print(df)

print("Column names:", df.columns)

print("Information about each row including data types:")
print("(note - type 'object' is catch-all that includes strings)")
print(df.info())

print("\nWe can extract a column of data as a Series object:")
print(df['Feature1'])

row = df.ix[0]
print("\nWe can extract a row as a Python dictionary:")
print(row)

print("\nRow items, e.g. Feature1={feature1}".format(feature1=row['Feature1']))
