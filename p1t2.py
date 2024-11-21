import numpy
import matplotlib.pyplot as plt

up=0
down=0
left=0
right=0

up_right=0
up_left=0
down_right=0
down_left=0

diag=None
diag_tot=0

X=None
Y=None
pos_X=0
pos_Y=0
X_vals=[]
Y_vals=[]

for i in range(100):
    diag = round(numpy.random.uniform(0,1))

    X = round(numpy.random.uniform(0,1))
    Y = round(numpy.random.uniform(0,1))

    if diag == 1:
        if X==1 and Y==1:
            up_right+=1
            pos_X+=1
            pos_Y+=1
        elif X==1 and Y==0:
            down_right+=1
            pos_X+=1
            pos_Y-=1
        elif X==0 and Y==1:
            up_left+=1
            pos_X-=1
            pos_Y+=1
        elif X==0 and Y==0:
            down_left+=1
            pos_X-=1
            pos_Y-=1
        diag_tot+=1
    else:
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


print(f"diag_tot= {diag_tot}")
print(f"up= {up} down={down} left={left} right={right}")
print(f"up_right= {up_right} down_right={down_right} up_left={up_left} down_left={down_left}")


plt.plot(X_vals, Y_vals, marker='o', markersize=3, color='grey', linestyle='-')
plt.grid(True)
plt.show()


directions = ["Up", "Down", "Left", "Right", "Up-Right", "Up-Left", "Down-Right", "Down-Left"]
counts = [up, down, left, right, up_right, up_left, down_right, down_left]

plt.bar(directions, counts, color='skyblue')
plt.title("Directional Movement Distribution")
plt.xlabel("Direction")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.show()
