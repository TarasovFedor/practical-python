# Exercise 2.22: Data Extraction

from os import path as ospath
from sys import path as syspath
other_dir = ospath.join(ospath.dirname(__file__), 'Other')
syspath.append(other_dir)
from portfolio_cost import read


portfolio = read('Work/Data/portfolio.csv')
name_shares = [(row['name'], row['shares']) for row in portfolio]

print(name_shares, end='\n\n')

names = {row['name'] for row in portfolio}
print(names, end='\n\n')