from example_package import example
from decimal import *
print(example.add_one(100))

getcontext().prec = 50
print(Decimal(1) / Decimal(7))