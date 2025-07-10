from os import path as ospath
from sys import path as syspath

other_dir = ospath.join('Work')
syspath.append(other_dir)
from report import read_portfolio as read
from report import color_text as color


def portfolio_cost(filename: str) -> float:
    '''Calculates cost of the portfolio from provided file'''
    portfolio = read(filename)
    total = sum([row['shares'] * row['price'] for row in portfolio])
    return total

if __name__ == '__main__':
    cost = portfolio_cost('Work/Data/portfolio.csv')
    print('Total cost is', cost)

    print(portfolio_cost('qwq'))