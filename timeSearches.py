import random
from lp import *
from binary_search import Binary_search
from linear_search import Linear_search
import time as t


find_val = 768
def binary_search_time(sum=0):
    for _ in range(0,4):
        start_time = t.time()
        b = Binary_search(n, find_val)
        end_time = t.time()
        full_time = end_time-start_time
        sum += full_time
    return sum /3

time = binary_search_time()
file = open("times/binarySearchtimes.txt", "a")
file.write(f"{time:.29f},\n")
print(f"binary search: {time:.29f}")

def linear_search_time(sum=0):
    for _ in range(0,4):
        start_time = t.time()
        v  = Linear_search(n, find_val)
        end_time = t.time()
        full_time = end_time-start_time
        sum += start_time
    return sum /3

time = linear_search_time()
file = open("times/linear_times.txt", "a")
file.write(f"{time:.29f},\n")
print(f"linear search: {time:.29f}")