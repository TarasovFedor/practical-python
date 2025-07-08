# Exercise 2.17: Inverting a dictionary

prices = {
    'GOOG' : 490.1,
    'AA' : 23.45,
    'IBM' : 91.1,
    'MSFT' : 34.23,
}

inverted_prices = dict(zip(prices.values(), prices.keys()))
print(inverted_prices)