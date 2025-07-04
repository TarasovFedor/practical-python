# pcost.py
#
# Exercise 1.27

total = 0

with open('D:\Документы\Коды\Курс по Пайтону\practical-python\Work\Data\portfolio.csv', 'rt') as file:
    next(file)
    for line in file:
        row = line.split(',')
        total += (int(row[1]) * float(row[2]))

print(f'Total cost is {total}')