# report.py
#
# Exercise 2.4

# from pprint import pprint
from typing import Any
from fileparse import parse_csv
import sys
import os
other_dir = os.path.join(os.path.dirname(__file__), 'Other')
sys.path.append(other_dir)
from read_prices import color_text
from stock import Stock


def read_portfolio(filename: str) -> list[Stock]:
    '''Parces provided portfolio.csv making a list of dictionaries with info from the portfolio.
    Portfolio should have "shares" and "price" columns'''

    try:
        with open(filename, 'rt') as file:
            stocks = parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float])
            stocks = [Stock(entry['name'], entry['shares'], entry['price']) for entry in stocks] # type: ignore
            return stocks
        
    except FileNotFoundError:
        print(color_text(f'No such file or directory: {filename}'))
        return []

def read_prices(filename: str) -> dict[str, float]:
    prices = {}

    try:
        with open(filename) as file:
            prices = dict(parse_csv(file, types=[str, float], has_headers=False)) # type: ignore
    except FileNotFoundError:
        print(color_text(f'No such file or directory: {filename}'))
    
    return prices # type: ignore


def make_report_data(portfolio: list[Stock], prices: dict[str, Any]) -> list[tuple[str, int, float, float]]:
    '''Makes a report about changes in prices of stocks from provided portfolio'''
    report = []

    for i in range(len(portfolio)):
        stock_name = portfolio[i].name
        stock_shares = portfolio[i].shares
        new_price = prices[stock_name]
        change = portfolio[i].price - new_price

        report.append((stock_name, stock_shares, new_price, change))

    return report

def print_report(reportdata: list[tuple[str, int, float, float]]) -> None:
    '''Prints provided report, which should contain "Name", "Shares", "Price" and "Change" values'''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(''.join(f'{h:>10s} ' for h in headers))
    print(('-'*10 + ' ') * len(headers))

    for name, shares, price, change in reportdata:
        print(f'{name:>10s} {shares:>10d} {("$"+str(price)):>10s} {change:>10.2f}')

def portfolio_report(datafile: str, pricefile: str = 'Work/Data/prices.csv', will_print: bool = False) -> list[tuple[str, int, float, float]]:
    '''Returns a report about changes in prices of stocks from provided portfolio.
    \nCan also print the report if "will_print" is True'''

    prices = read_prices(pricefile)

    portfolio = read_portfolio(datafile)
    report = make_report_data(portfolio, prices)

    if will_print:
        print_report(report)

    return report

portfolio_report('Work/Data/portfolio.csv', will_print=True)