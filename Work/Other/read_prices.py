# from pprint import pprint

def color_text(*text: str, color_code: int = 244) -> str:
    '''Colors provided text with the specified color (grey by default)'''
    return f"\033[38;5;{color_code}m{text}\033[0m"

def str_clean(string: str) -> str:
    '''"Cleans" provided string using .strip method and deleting double quotes'''
    return string.strip().replace('"', '')

def read_prices(filename: str) -> dict[str, float]:
    '''Reads prices from provided .csv file'''
    prices = {}

    with open(filename, 'rt') as file:
        for i, line in enumerate(file, start=1):
            line = [str_clean(s) for s in line.split(',')]
            try:
                prices[line[0]] = float(line[1])
            except IndexError:
                print(color_text(f'IndexError raised by value that belongs to {line[0]!r} in line {i}'))
            except ValueError:
                print(color_text(f'Could not convert value {line[1]!r} to float; the value belongs to {line[0]!r} in line {i}'))

    return prices

# prices = read_prices('Work/Data/prices.csv')
# pprint(prices)