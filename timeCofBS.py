import random as r

l = r.randint(0, 999999)
print(f"start length of l is: {l}")
while True:
    input()
    l //=2
    print(l)