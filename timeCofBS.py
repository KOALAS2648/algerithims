import matplotlib.pyplot as plt
import random as r

l = r.randint(0, 999999)
x =[]
y= []
n=0
while l != 0:
    
    l //=2
    
    x.append(l)
    y.append(n)
    n+=1
# x axis values

# corresponding y axis values

# plotting the points 
plt.plot(x, y)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()