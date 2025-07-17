# report.py
#
# Exercise 2.4

from typing import Any
from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
import tableformat

def color_text(text: str, color_code: int = 244) -> str:
    '''Colors provided text with the specified color (grey by default)'''
    return f"\033[38;5;{color_code}m{text}\033[0m"


def read_portfolio(filename: str) -> Portfolio:
    '''Parces provided portfolio.csv making a list of dictionaries with info from the portfolio.
    Portfolio should have "shares" and "price" columns'''

    try:
        with open(filename, 'rt') as file:
            stocks = Portfolio.from_csv(file)
            # stocks = parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float])
            # stocks = [Stock(**entry) for entry in stocks] # type: ignore
        
    except FileNotFoundError:
        print(color_text(f'No such file or directory: {filename}'))
        stocks = Portfolio()
    
    return stocks

def read_prices(filename: str) -> dict[str, float]:
    prices = {}

    try:
        with open(filename) as file:
            prices = dict(parse_csv(file, types=[str, float], has_headers=False)) # type: ignore
    except FileNotFoundError:
        print(color_text(f'No such file or directory: {filename}'))
    
    return prices # type: ignore


def make_report_data(portfolio: Portfolio, prices: dict[str, Any]) -> list[tuple[str, int, float, float]]:
    '''Makes a report about changes in prices of stocks from provided portfolio'''
    report = []

    for i in range(len(portfolio)):
        stock_name = portfolio[i].name
        stock_shares = portfolio[i].shares
        new_price = prices[stock_name]
        change = new_price - portfolio[i].price

        report.append((stock_name, stock_shares, new_price, change))

    return report

def print_report(reportdata: list[tuple[str, int, float, float]], formatter: tableformat.TableFormatter, format: str = 'text table') -> None:
    '''Prints provided report, which should contain "Name", "Shares", "Price" and "Change" values'''
    formatter.headings(('Name', 'Shares', 'Price', 'Change'))

    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(datafile: str, pricefile: str = 'Work/Data/prices.csv', will_print: bool = False, format: str = 'txt') -> list[tuple[str, int, float, float]]:
    '''Returns a report about changes in prices of stocks from provided portfolio.
    \nCan also print the report if "will_print" is True'''

    portfolio = read_portfolio(datafile)
    prices = read_prices(pricefile)

    report = make_report_data(portfolio, prices)

    if will_print:
        formatter = tableformat.create_formatter(format)
        print_report(report, formatter)

    return report


portfolio = read_portfolio('Work/Data/portfolio.csv')
print(portfolio)
# frmt = tableformat.create_formatter('html')
# tableformat.print_table(portfolio, frmt, ['name', 'price'])
# portf = portfolio_report('Work/Data/portfolio.csv', will_print=True, format='csv')