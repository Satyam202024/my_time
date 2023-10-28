import pandas as pd

df = pd.read_csv('data.csv',nrows=0)
header = df.columns.tolist()
print(*header)
# print(df) 
# print(df['Duration'].to_string(index=False))
# print(df['Pulse'].to_string(index=False))