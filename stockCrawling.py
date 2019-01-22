import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2015,1,1)
end = datetime.datetime(2018,1,1)

code = "078930.KS" # 종목코드
timeSeries = web.DataReader(code, 'yahoo', start, end)

plt.plot(timeSeries[timeSeries.columns[2]])
plt.show()
