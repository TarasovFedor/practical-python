bill_thickness = 0.11 * 0.001
sears_height = 442 
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(f'day {day}: bills height = {num_bills * bill_thickness}; sears height = {sears_height}')
    day += 1
    num_bills *= 2

print(f'final height is {num_bills * bill_thickness}, it took {day} days')