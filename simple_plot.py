url = "http://chart.finance.yahoo.com/table.csv?s=GE&a=7&b=14&c=2016&d=8&e=14&f=2016&g=d&ignore=.csv"
import urllib2
ge_csv = urllib2.urlopen(url)
import pandas as pd
ge = pd.read_csv(ge_csv, index_col = 0, parse_dates = True)
%matplotlib inline
from matplotlib.pyplot import plot
ge.plot(y = 'Adj Close')
