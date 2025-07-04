# bounce.py

# Exercise 1.5

height = 100
multiplier = 0.6

for i in range(1, 11):
    height = round(height * multiplier, 4)
    print(i, height)