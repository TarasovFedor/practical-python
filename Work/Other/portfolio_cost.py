def portfolio_cost(filename: str):
    try:
        total = 0.0

        with open(filename, 'rt') as file:
            next(file)
            for line in file:
                row = line.split(',')
                total += (int(row[1]) * float(row[2]))

        return total
    except FileNotFoundError:
        print('No such file or directory:', f'\'{filename}\'')
        return 0.0

cost = portfolio_cost('D:\Документы\Коды\Курс по Пайтону\practical-python\Work\Data\portfolio.csv')
print('Total cost is', cost)

print(portfolio_cost('qwq'))