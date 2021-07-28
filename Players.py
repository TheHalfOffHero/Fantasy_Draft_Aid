import pandas as pd

df=pd.read_csv('TenTeamStandardBeerSheet.csv', encoding='us-ascii');

print(df.to_string());