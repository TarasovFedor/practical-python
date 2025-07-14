# pcost.py
#
# Exercise 1.27

import os
import sys
other_dir = os.path.join(os.path.dirname(__file__), 'Other')
sys.path.append(other_dir)
from read_prices import color_text, str_clean


def portfolio_cost(filename: str) -> float:
    total = 0

    with open(filename, 'rt') as file:
        headers = [str_clean(s) for s in next(file).split(',')]

        for i, line in enumerate(file, start=1):
            row = line.split(',')
            row = list(map(str_clean, row))
            row = dict(zip(headers, row))

            try:
                shares = int(row['shares'])
                price = float(row['price'])
                total += (shares * price)

            except ValueError:
                print(color_text(f'Could not parse line {i}: {row}'))

    # print(f'Total cost is {total}')
    return total

def file_check(filename: str, error_message: str = 'Value is missing on line: ') -> None:
    with open(filename, 'rt') as file:
        next(file)
        for i, line in enumerate(file, start=1):
            row = line.split(',')
            try:
                row = (row[0], int(row[1]), float(row[2]))
            except ValueError:
                print(error_message, i)


# file_check('Work/Data/missing.csv')
print(portfolio_cost('Work/Data/portfoliodate.csv'))