from os import path as ospath
from sys import path as syspath
syspath.append(ospath.join('Work'))
import report

def stock_name(s):
    return s.name


portfolio = list(report.read_portfolio('Work/Data/portfolio.csv'))
# portfolio.sort(key=stock_name)
portfolio.sort(key=lambda s: s.price)

for entry in portfolio:
    print(entry)