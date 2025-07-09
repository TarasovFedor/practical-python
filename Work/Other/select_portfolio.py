import csv
from typing import Any
from read_prices import color_text as color

def select_portfolio(filename: str, select: list[str] = ['name', 'shares', 'price']) -> list[dict[str, Any]] | list[None]:
    '''Selects stated columns from provided .csv file'''
    try:
        with open(filename, 'rt') as file:
            rows = csv.reader(file)

            headers = next(rows)
            indicies = [headers.index(colname) for colname in select]
            portfolio = [{colname: row[index] for colname, index in zip(select, indicies)} for row in rows]

        return portfolio
    
    except FileNotFoundError:
        print(color('No such file or directory:'), color(f"'{filename}'"))
    except KeyError:
        print(color(f'Couldn\'t find column "shares" and/or column "price" in provided portfolio'))
    except ValueError:
        # print(color(f'Couldn\'t convert shares or price into numeric types in this row: \n{row}'))
        print(color(f'Couldn\'t convert "shares" or "price" value into numeric types'))
    return []

print(select_portfolio('Work/Data/portfoliodate.csv'))