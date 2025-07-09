from os import path as ospath
from sys import path as syspath

other_dir = ospath.join('Work')
syspath.append(other_dir)
from report import read_portfolio as read
from report import color_text as color
from report import str_clean as clean


def portfolio_cost(filename: str) -> float:
    '''Calculates cost of the portfolio from provided file; returns 0.0 if file is incorrect or doesn't exist'''
    try:
        portfolio = read(filename)
        total = sum([row['shares'] * row['price'] for row in portfolio])
        return total
    
    except FileNotFoundError:
        print(color('No such file or directory:'), color(f"'{filename}'"))
    except KeyError:
        print(color(f'Couldn\'t find column "shares" and/or column "price" in provided portfolio'))
    except ValueError:
        # print(color(f'Couldn\'t convert shares or price into numeric types in this row: \n{row}'))
        print(color(f'Couldn\'t convert "shares" or "price" value into numeric types'))
    return 0.0

if __name__ == 'main':
    cost = portfolio_cost('Work/Data/portfolio.csv')
    print('Total cost is', cost)

    print(portfolio_cost('qwq'))