def portfolio_cost(filename: str):
    try:
        total = 0.0

        with open(filename, 'rt') as file:
            headers = next(file)
            for row in file:
                shares = int(row[1])
                price = float(row[2])
                total += (shares * price)
        return total
    
    except FileNotFoundError:
        print('No such file or directory:', f"'{filename}'")
        return 0.0

cost = portfolio_cost('Work/Data/portfolio.csv')
print('Total cost is', cost)

print(portfolio_cost('qwq'))