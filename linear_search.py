def Linear_search(l:list, target:any, n=0):
    n = 0
    if n > len(l):
        return False
    for i in range(len(l)):
        if l[n] == target:
            return n
        n +=1
if __name__ == "__main__":
    n = [9,8,7,6,5,4,3,2,1]
    print(Linear_search(n, 2))