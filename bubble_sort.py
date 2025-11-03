def Bubble_sort(l:list):
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

n = [9,8,7,6,5,4,3,2,1]

print(Bubble_sort(n))