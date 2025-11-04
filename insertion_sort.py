def Insertion_sort(l:list):
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j+1] < l[j]:
                l.insert(j, l.pop(j+1))
    return l

if __name__ == "__main__":
    n = [9,8,7,6,5,4,3,2,1]
    print(Insertion_sort(n))