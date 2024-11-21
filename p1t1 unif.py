import numpy
import matplotlib.pyplot as plt
up=0
down=0
left=0
right=0

X=None
Y=None

pos_X=0
pos_Y=0

X_vals=[]
Y_vals=[]

for i in range(100):
    X = round(numpy.random.uniform(0,1))
    Y = round(numpy.random.uniform(0,1))
    if X==1 and Y==1:
        up+=1
        pos_Y+=1
    elif X==1 and Y==0:
        down+=1
        pos_Y-=1
    elif X==0 and Y==1:
        left+=1
        pos_X-=1
    elif X==0 and Y==0:
        right+=1
        pos_X+=1
 
    X_vals.append(pos_X)
    Y_vals.append(pos_Y)


print(f"up= {up} down={down} left={left} right={right}")

plt.plot(X_vals, Y_vals, marker='o', markersize=3, color='grey', linestyle='-')
plt.grid(True)
plt.show()
