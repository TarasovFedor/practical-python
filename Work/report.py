# report.py
#
# Exercise 2.4
# from pprint import pprint

import sys
import os
other_dir = os.path.join(os.path.dirname(__file__), 'Other')
sys.path.append(other_dir)
import read_prices


def read_portfolio(filename: str) -> list[dict[str, float]]:
    portfolio = []
    rows = []

    with open(filename, 'rt') as file:
        # headers = list(map(lambda a: a.strip(), next(file).split(',')))
        headers = [s.strip() for s in next(file).split(',')]

        for row in file:
            row = tuple(row.split(','))
            row = (read_prices.str_clean(row[0]), int(row[1]), float(row[2]))
            rows.append(row)

        for i in range(len(rows)):
            line = {}
            
            for j in range(len(headers)):
                line[headers[j]] = rows[i][j]
            
            portfolio.append(line)

    return portfolio

# print(read_portfolio('Work/Data/portfolio.csv'))
# pprint(read_portfolio('Work/Data/portfolio.csv'))

portfolio = read_portfolio('Work/Data/portfolio.csv')
prices = read_prices.read_prices('Work/Data/prices.csv')

difference = 0
for i in range(len(portfolio)):
    stock_name = portfolio[i]['name']
    stock_shares = portfolio[i]['shares']

    spent = portfolio[i]['price'] * stock_shares
    possible_income = prices[stock_name] * stock_shares # type: ignore

    difference += possible_income - spent

print(difference)