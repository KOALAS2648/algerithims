import random
from lp import *
from binary_search import Binary_search
from linear_search import Linear_search
import time as t
import os

find_val = 7933
TIMES = 10000
print(f"trying to find:{find_val}")

def binary_search_time(sum=0):
    done_times = 0
    for _ in range(0,TIMES+1):
        start_time = t.perf_counter()
        b = Binary_search(n, find_val)
        end_time = t.perf_counter()
        full_time = end_time-start_time
        sum += full_time
        print("binary serach")
        print(f"amount done:{(done_times/TIMES)*100:.1f}%")
        done_times +=1
        os.system("clear")
        
    return sum /TIMES
b=[]
timeBS = binary_search_time()
file = open("times/binarySearchtimes.txt", "a")
file.write(f"{timeBS:.29f}: averaged over {TIMES},\n ")

def linear_search_time(sum=0):
    done_times = 0
    for _ in range(0,TIMES+1):
        start_time = t.perf_counter()
        v  = Linear_search(n, find_val)
        end_time = t.perf_counter()
        full_time = end_time-start_time
        sum += full_time
        print("linear serach")
        print(f"amount done:{(done_times/TIMES)*100:.1f}%")
        done_times +=1
        os.system("clear")
    return sum /TIMES

time = linear_search_time()
file = open("times/linear_times.txt", "a")
file.write(f"{time:.29f}: averaged over {TIMES},\n")
print(f"binary search: {timeBS:.29f}: averaged over {TIMES} times")
print(f"linear search: {time:.29f}: averaged over {TIMES} times")