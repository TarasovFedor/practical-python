prices = {}

with open('Work/Data/prices.csv', 'rt') as file:
    for line in file:
        line = line.split(',')
        try:
            prices[line[0]] = float(line[1])
        except IndexError:
            continue

print(prices)