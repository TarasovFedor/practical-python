from collections import Counter
from stock import Stock

class Portfolio:
    __slots__ = ('_holdings')

    def __init__(self, holdings: list[Stock]):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()
    
    def __len__(self):
        return len(self._holdings)
    
    def __getitem__(self, index: int) -> Stock:
        return self._holdings[index]
    
    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

    @property
    def total_cost(self):
        '''Sum of costs of all stocks in the holding'''
        return sum(s.cost for s in self._holdings)
    
    def tabulate_shares(self) -> Counter:
        total_shares = Counter()

        for s in self._holdings:
            total_shares[s.name] += s.shares
        
        return total_shares