from collections import Counter
from stock import Stock
from fileparse import parse_csv

class Portfolio:
    __slots__ = ('_holdings')

    def __init__(self):
        self.holdings = []

    @property
    def holdings(self):
        return self._holdings
    
    @holdings.setter
    def holdings(self, value):
        self._holdings = value

    def __iter__(self):
        return self.holdings.__iter__()
    
    def __len__(self):
        return len(self.holdings)
    
    def __getitem__(self, index: int) -> Stock:
        return self.holdings[index]
    
    def __contains__(self, name):
        return any(s.name == name for s in self.holdings)
    
    def __str__(self):
        return '\n'.join(str(holding) for holding in self.holdings)

    @property
    def total_cost(self):
        '''Sum of costs of all stocks in the holding'''
        return sum(s.cost for s in self.holdings)
    
    def append(self, holding):
        if not isinstance(holding, Stock):
            raise TypeError('Expected a Stock instance')
        self.holdings.append(holding)

    def tabulate_shares(self) -> Counter:
        total_shares = Counter()

        for s in self.holdings:
            total_shares[s.name] += s.shares
        
        return total_shares
    
    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = parse_csv(lines,
                              select=['name', 'shares', 'price'],
                              types=[str, int, float],
                              **opts)
        for d in portdicts:
            self.append(Stock(**d)) # type: ignore

        return self
    

if __name__ == '__main__':
    with open('Work/Data/portfolio.csv') as file:
        port = Portfolio.from_csv(file)
        print(port)