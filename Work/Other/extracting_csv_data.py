import csv
from pprint import pprint

file = open('Work/Data/portfoliodate.csv')
rows = csv.reader(file)
headers = next(rows)

select = ['name', 'shares', 'price']

indicies = [headers.index(colname) for colname in select]
portfolio = [{colname: row[index] for colname, index in zip(select, indicies)} for row in rows]

pprint(portfolio)

file.close()