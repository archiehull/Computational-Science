import numpy as np
import matplotlib.pyplot as plt

# Parameters
k = 0.006  # Growth rate
M = 10**13  # Carrying capacity
N0 = 10**9  # Initial tumor cell population
h = 0.1  # Step size
t_max = 1200  # Maximum time
time = np.arange(0, t_max, h)  # Time array

# Gompertz model implementation
def gompertz_growth(N, k, M):
    return k * N * np.log(M / N)

def simulate_growth(N0, M, k, h, max_time=1200):
    time = 0
    N = [N0]

    while N[-1] < M * 0.99:  # Relative error condition
        dN = h * gompertz_growth(N[-1], k, M)
        N.append(N[-1]+dN)
        time += h

        if time > max_time:  # Safeguard against infinite loops
            print("Warning: Reached maximum simulation time without convergence.")
            break
    return time  # Return time taken to reach steady state


# Movement
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

current_pos=0,0

XY_vals=[]

spread=0
cell_no=10

directional_moves=[[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1],[1,1],[-1,-1]]

for i in range(1200):    
    steady_time = simulate_growth(N0, M, k, h)

    print(i)
    while(True):

        diag = round(np.random.uniform(0,1))

        X = round(np.random.uniform(0,1))
        Y = round(np.random.uniform(0,1))

        old_x = pos_X
        old_y = pos_Y

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
        
        current_pos=pos_X,pos_Y

        if current_pos not in XY_vals:
            break    

        #if current_pos is in 
        #print("cell occupied")

    X_vals.append(pos_X)
    Y_vals.append(pos_Y)
    XY_vals.append(current_pos)




plt.plot(X_vals, Y_vals, marker='o', markersize=3, color='grey', linestyle='-')
plt.grid(True)
plt.show()
