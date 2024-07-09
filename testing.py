from timeit import timeit
from functions import *

# measure the time taken for 50 repetitions
print(timeit('read_file("data/wundertuete0.txt")', number=50, globals={'read_file': read_file}))