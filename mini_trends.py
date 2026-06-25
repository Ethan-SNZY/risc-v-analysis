from pytrends.request import TrendReq
import pandas as pd

#Connection to Google Trends
pytrends = TrendReq(hl='en-US', tz=360)

#Search payload & terms
search_terms = ['RISC-V', 'ARM architecture', 'x86']
pytrends.build_payload(search_terms, timeframe ="today 12-m", geo="")

#Fetch Data
df = pytrends.interest_over_time()

print(df.head())
print(df.tail())

#Clean up + Save
df = df.drop(columns=['isPartial'], errors ='ignore')
df = df.reset_index()
df.rename(columns={'Date': 'week_date'})

df.to_csv('trends.csv', index=False)
print("Saved to trends.csv")    