from calculations import *
import time

start = time.time()

unit_fraction = 0.0
d = 1

while d < 1000:
    unit_fraction = 1/d
print()

print(time.time() - start, 'seconds')
