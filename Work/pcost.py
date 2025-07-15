# pcost.py
#
# Exercise 1.27

from report import read_portfolio


def portfolio_cost(filename: str) -> float:
    '''Computes the total cost, which is shares*price, of a portfolio file'''

    portfolio = read_portfolio(filename)

    return sum((entry.cost for entry in portfolio))