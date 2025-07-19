from typedproperty import String, Integer, Float


class Stock:
    '''Class that represents a single holding of stock consisting of name, shares and price.'''
    __slots__ = ('_name', '_shares', '_price')

    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    
    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self) -> float:
        '''Returns cost of the holding'''
        return self.shares * self.price
    
    def sell(self, amount: int) -> None:
        '''"Sells" provided amount of the stock'''
        self.shares -= amount

    def __str__(self) -> str:
        return f'Name: {self.name}, shares: {self.shares}, price: ${self.price}'

    def __repr__(self) -> str:
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"

class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)


# if __name__ == '__main__':
    # with open('Work/Data/portfolio.csv') as rows:
    #     portdicts = parse_csv(rows, select=['name', 'shares', 'price'], has_headers=True, types=[str, int, float])
        
    # portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts] #type: ignore

    # portfolio[0] = MyStock(portfolio[0].name, portfolio[0].shares, portfolio[0].price)
    # portfolio[0].panic()
    # print(portfolio[0].shares)
    # st = Stock('QWQ', 120, 13.37)
    # print(repr(st))
    # st2 = eval(repr(st))
    # print(st2)
    # st = Stock('QWQ', 120, 13.37)
    # print(st.cost)