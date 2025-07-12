# fileparse.py
#
# Exercise 3.3
import csv
from typing import Type, Union, Any

from os import path as ospath
from sys import path as syspath

other = ospath.join(ospath.dirname(__file__), 'Other')
syspath.append(other)
from read_prices import color_text as color


def parse_csv(
        filename: str, select: list[str] = [], types: list[Type[Any]] = [], has_headers: bool = False, delimeter: str = ','
        ) -> list[dict[str, Union[str, int, float]]] | list[tuple[Union[str, int, float]]]:
    '''Parse a .csv file into a list of records. Can select and return only specified columns, ignores names from provided "select" that are not in headers of the table.'''
    
    records = []
    try:
        with open(filename) as file:
            rows = csv.reader(file, delimiter=delimeter)

            if has_headers:
                headers = next(rows)
                indices = []
                if select:
                    select = [colname for colname in select if colname in headers]

                    for colname in select:
                        indices.append(headers.index(colname))

                    headers = select
                else:
                    indices = []
                    select = []
            
                for lineind, row in enumerate(rows, start=1):
                    if not row:
                        continue
                    
                    try:
                        if indices:
                            row = [row[index] for index in indices]
                    except IndexError:
                        print(color(f'Index error has occured in line {lineind}, row {row!r} is skipped'))
                        continue

                    if types:
                        try:
                            row = [func(val) for func, val in zip(types, row)]
                        except ValueError:
                            print(color(f'Could not convert values of the row {row!r} into types {types}, line {lineind} as skipped'))
                            continue

                    record = dict(zip(headers, row))
                    records.append(record)
            else:
                for lineind, row in enumerate(rows, start=1):
                    if not row:
                        continue

                    if types:
                        try:
                            row = [func(val) for func, val in zip(types, row)]
                        except ValueError:
                            print(color(f'Could not convert values of the row {row!r} into types {types}, line {lineind} as skipped'))
                            continue
                    
                    record = tuple(row)
                    records.append(record)
    except FileNotFoundError:
        print(color(f'No such file found:\n{filename!r}'))

    return records


portfolio = parse_csv('Work/Data/portfolio.csv', has_headers=False, select=['name'], types=[str, int, float])
print(portfolio)