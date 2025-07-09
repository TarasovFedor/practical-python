# Exercise 2.18: Tabulating with Counters
from collections import Counter
from pprint import pprint
from typing import Any

import os
import sys
other_dir = os.path.join('Work')
sys.path.append(other_dir)
from report import read_portfolio

def holdings_counter(portfolio: list[dict[str, Any]]) -> Counter[dict[str, int | Any]]:
    holdings = Counter()

    for s in portfolio:
        holdings[s['name']] += s['shares']

    return holdings

portfolio = read_portfolio('Work/Data/portfolio.csv')
holdings = holdings_counter(portfolio)
portfolio2 = read_portfolio('Work/Data/portfolio2.csv')
holdings2 = holdings_counter(portfolio2)

pprint(holdings)
print()
pprint(holdings2)

combined = holdings + holdings2