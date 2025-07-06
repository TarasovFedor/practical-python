# import os
from pprint import pprint
# print(os.getcwd())

table = {}
contents = []
# with open(os.getcwd()+'//'+'Work\Data\portfolio.csv', 'rt') as file:
with open('Work/Data/portfolio.csv', 'rt') as file:
    for line in file:
        headers = tuple(line.split(','))
        headers = tuple(el.strip() for el in headers)
        break

    for line in file:
        row = line.split(',')
        row[1] = int(row[1]) # type: ignore
        row[2] = float(row[2]) # type: ignore
        contents.append(row)
    
for i in range(len(headers)):
    table[headers[i]] = tuple(el[i] for el in contents)

pprint(table)