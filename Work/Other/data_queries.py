# Exercise 2.21: Data Queries

from os import path as ospath
from sys import path as syspath
other_dir = ospath.join(ospath.dirname(__file__), 'Other')
syspath.append(other_dir)
from portfolio_cost import read


portfolio = read('Work/Data/portfolio.csv')

more100 = [row for row in portfolio if row['shares'] > 100]
print(more100)
print()

msft_ibm = [row for row in portfolio if row['name'] in ('MSFT', 'IBM')]
print(msft_ibm)
print()

cost10k = [row for row in portfolio if row['shares'] * row['price'] > 10000]
print(cost10k)