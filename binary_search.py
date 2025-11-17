import random
import time as t
def Binary_search(l:list, target:any):
        middle_idx = len(l) //2
        if l[middle_idx] == target:
            return True
        if l[middle_idx] > target:
            return Binary_search(l[:middle_idx], target)
        if l[middle_idx] < target:
            return Binary_search(l[middle_idx+1:], target)
    else:
        return True
    
if __name__ == "__main__":
    n = [random.randrange(0, 1000) for i in range(1000)]
    n.sort()
    find_val = random.randint(0, 1000)

    print(f"{Binary_search(n, find_val)}")
