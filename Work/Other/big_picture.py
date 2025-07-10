import csv
from pprint import pprint


types = [str, float, (lambda s: tuple(map(int,s.split('/')))), str, float, float, float, float, int]

with open('Work/Data/dowstocks.csv', 'rt') as file:
    rows = csv.reader(file)

    headers = next(rows)
    
    converted = [{key: value for key, value in zip(headers, row)} for row in [[func(value) for func, value in zip(types, row)] for row in rows]] # weird abomination

    pprint(converted)