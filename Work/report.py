# report.py
#
# Exercise 2.4

from pprint import pprint
from typing import Any
import sys
import os
other_dir = os.path.join(os.path.dirname(__file__), 'Other')
sys.path.append(other_dir)
from read_prices import color_text, read_prices, str_clean


def read_portfolio(filename: str) -> list[dict[str, Any]]:
    '''Parces provided portfolio.csv making a list of dictionaries with info from the portfolio. Portfolio should have "shares" and "price" columns'''
    portfolio = []

    try:
        with open(filename, 'rt') as file:
            # headers = list(map(lambda a: a.strip(), next(file).split(',')))
            headers = [str_clean(s) for s in next(file).split(',')]

            for row in file:
                row = (str_clean(s) for s in row.split(','))
                
                row = dict(zip(headers, row))

                row['shares'] = int(row['shares']) # type: ignore
                row['price'] = float(row['price']) # type: ignore
                
                portfolio.append(row)

    except FileNotFoundError:
        print(color_text(f'No such file or directory: {filename}'))
    except ValueError:
        print(color_text(f'Couldn\'t convert "shares" or "price" into numeric types in this row: \n{row}'))
    except KeyError:
        print(color_text(f'Couldn\'t find column "shares" and/or column "price" in provided portfolio'))

    return portfolio
        # for i in range(len(rows)):
        #     line = {}
            
        #     for j in range(len(headers)):
        #         line[headers[j]] = rows[i][j]
            
        #     portfolio.append(line)


def make_report(portfolio: list[dict[str, Any]], prices: dict[str, Any]) -> list[tuple[str, int, float, float]]:
    '''Makes a report about changes in prices of stocks from provided portfolio'''
    report = []

    for i in range(len(portfolio)):
        stock_name = portfolio[i]['name']
        stock_shares = portfolio[i]['shares']
        new_price = prices[stock_name]
        change = new_price - portfolio[i]['price']

        report.append((stock_name, stock_shares, new_price, change))

    return report

def print_report(report: list[tuple[str, int, float, float]]) -> None:
    '''Prints provided report, which should contain "Name", "Shares", "Price" and "Change" values'''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(''.join(f'{h:>10s} ' for h in headers))
    print('-'*10 + ' ' + '-'*10 + ' ' + '-'*10 + ' ' + '-'*10)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {("$"+str(price)):>10s} {change:>10.2f}')

def portfolio_report(filenames: list[str], prices: str = 'Work/Data/prices.csv') -> tuple[list[tuple[str, int, float, float]]]:
    '''Returns a tuple of reports about changes in prices of stocks from provided portfolios'''
    reports = []
    
    for filename in filenames:
        report = make_report(read_portfolio(filename), read_prices(prices))
        reports.append(report)

    return tuple(reports)


if __name__ == '__main__':
    # portfolio = read_portfolio('Work/Data/portfolio.csv')
    # portfolio = read_portfolio('Work/Data/portfoliodate.csv')
    # prices = read_prices('Work/Data/prices.csv')

    # report = make_report(portfolio, prices)

    reports = portfolio_report(['Work/Data/portfolio.csv', 'Work/Data/portfoliodate.csv'])
    print(reports)

    for report in reports:
        print_report(report)
        print()


# print(read_portfolio('Work/Data/portfolio.csv'))
# pprint(read_portfolio('Work/Data/portfolio.csv'))

# pprint(make_report(portfolio, prices))

# difference = 0
# for i in range(len(portfolio)):
#     stock_name = portfolio[i]['name']
#     stock_shares = portfolio[i]['shares']

#     spent = portfolio[i]['price'] * stock_shares
#     possible_income = prices[stock_name] * stock_shares # type: ignore

#     difference += possible_income - spent

# print(difference)