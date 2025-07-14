# from fileparse import parse_csv


class Stock:
    '''Class that represent a single holding of stock'''
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self) -> float:
        '''Returns cost of the holding'''
        return self.shares * self.price
    
    def sell(self, amount: int) -> None:
        '''"Sells" provided amount of the stock'''
        self.shares -= amount

# if __name__ == '__main__':
#     with open('Work/Data/portfolio.csv') as rows:
#         portdicts = parse_csv(rows, select=['name', 'shares', 'price'], has_headers=True, types=[str, int, float])
        
#     portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts] #type: ignore

#     for entry in portfolio:
#         print(entry.name, entry.shares, entry.price)