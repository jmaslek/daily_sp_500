import pandas as pd
import yfinance as yf
import time

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
sp_ticks = df["Symbol"].to_list()
sp_ticks_forYF = [tick.replace(".","-") for tick in sp_ticks]

closes = pd.DataFrame()
for idx in tqdm.tqdm(range(0,len(sp_ticks_forYF),20)):
    df = yf.download(sp_ticks_forYF[idx:idx+20],period="1y", progress=False)["Adj Close"]
    closes = pd.concat([df, closes], axis=1)
    time.sleep(.5)
    
df.to_csv("SP500_prices_1yr.csv")
