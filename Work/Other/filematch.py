def filematch(filename, substr):
    with open(filename) as file:
        for line in file:
            if substr in line:
                yield line

for line in filematch('Work/Data/portfolio.csv', 'MSFT'):
    print(line)