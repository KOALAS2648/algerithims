n = [9,8,7,6,5,4,3,2,1]
def binary_search(l:list, target:any, swapped=False):
    if not swapped:
        middle_idx = len(l) //2
        if l[middle_idx] == target:
            return True
        if l[middle_idx] > target:
            return binary_search(l[:middle_idx], target, True)
        if l[middle_idx] < target:
            return binary_search(l[middle_idx+1:], target,)
    else:
        return True

n.sort()
print(binary_search(n, 10))