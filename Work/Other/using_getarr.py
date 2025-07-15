from os import path as ospath
from sys import path as syspath
other = ospath.join('Work')
syspath.append(other)
import stock

s = stock.Stock('GOOG', 100, 490.1)
columns = ['name', 'shares']

for colname in columns:
    print(colname, '=', getattr(s, colname))