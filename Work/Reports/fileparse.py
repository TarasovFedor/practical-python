# fileparse.py
#
# Exercise 3.3
import csv
from typing import Iterable, Type, Any
# import logging
# log = logging.getLogger(__name__)

from os import path as ospath
from sys import path as syspath

other = ospath.join('Work')
syspath.append(other)
from Other.read_prices import color_text as color


def parse_csv(
        iterable: Iterable, select: list[str] = [], types: list[Type[Any]] = [], has_headers: bool = True, delimeter: str = ','
        ) -> list[dict[str, str | int | float]] | list[tuple[str | int | float]]:
    '''Parse file-like iterable object into a list of records. Can select and return only specified columns, ignores names from provided "select" that are not in headers of the table.'''
    
    if select and not has_headers:
        raise RuntimeError('"select" requires column headers')

    records = []
    
    try:
        if type(iterable) == str:
            raise TypeError

        rows = csv.reader(iterable, delimiter=delimeter)

        headers = next(rows) if has_headers else []

        if select:
            select = [colname for colname in select if colname in headers]
            indices = [headers.index(colname) for colname in select]
            headers = select
        
        for lineind, row in enumerate(rows, start=1):
            if not row:
                continue
            
            try:
                if select:
                    row = [row[index] for index in indices]
            except IndexError as e:
                print(color(f'Index error has occured in line {lineind}, row {row!r} is skipped'))
                continue
                # log.warning(f'Index error has occured in line {lineind}, row {row!r} is skipped')
                # log.debug(f'Reason: {e}')

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    print(color(f'Could not convert values of the row {row!r} into types {types}, line {lineind} as skipped'))
                    continue
                    # log.warning(f'Could not convert values of the row {row!r} into types {types}, line {lineind} as skipped')
                    # log.debug(f'Reason: {e}')

            record = dict(zip(headers, row)) if headers else tuple(row)

            records.append(record)

    except TypeError as e:
        print(color(f'Provided object "{iterable!r}" is not iterable or can not be processed'))
        # log.warning(f'Provided object "{iterable!r}" is not iterable or can not be processed')
        # log.debug(f'Reason: {e}')

    return records


# if __name__ == '__main__':
#     logging.basicConfig()
#     logging.getLogger('fileparse').setLevel(logging.DEBUG)
    # with open('Work/Data/missing.csv') as file:
    #     portfolio = parse_csv(file, has_headers=True, select=[], types=[str, int, float])
    # print(portfolio)

    # print(parse_csv('Work/Data/portfolio.csv'))
    # with open('Work/Data/prices.csv') as file:
    #     print(parse_csv(file, types=[str, float], has_headers=False))