from pytrends.request import TrendReq
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

%matplotlib inline

pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload(kw_list = ["Java Android", "Kotlin Android"], timeframe='today 5-y')
df = pytrends.interest_over_time().iloc[:-1,:]


fig = matplotlib.pyplot.figure(figsize=(15,8))

x = list(df.index)

plot_y1 = plt.plot(x, df['Java Android'], label = 'Java Android')
plot_y2 = plt.plot(x, df['Kotlin Android'], label = 'Kotlin Android')
plot_y3 = plt.axvline(np.datetime64('2017-05-15'), color = 'r', linewidth = 0.7, label = 'Google I/O 2017')

show_legend = plt.legend()
show_title = plt.title ('Google Trends : Java Android VS Kotlin Android')
show_xaxis = plt.xlabel('Date')
show_yaxis = plt.ylabel('Popularité')