import numpy as np
import matplotlib.pyplot as plt
import random


# Parameters
k = 0.006  # Growth rate
M = 10**13  # Carrying capacity
N0 = 10**9  # Initial tumor cell population
h = 1  # Step size
t_max = 1200  # Maximum time
time = np.arange(0, t_max, h)  # Time array

# Gompertz model implementation
def gompertz_growth(N, k, M):
    return k * N * np.log(M / N)

def simulate_growth(N0, M, k, h, max_time=1200):
    time = 0
    N = [N0]

    while N[-1] < M * 0.66:  # Relative error condition
        dN = h * gompertz_growth(N[-1], k, M)
        N.append(N[-1]+dN)
        time += h

        if time > max_time:  # Safeguard against infinite loops
            print("Warning: Reached maximum simulation time without convergence.")
            break
    return time  # Return time taken to reach steady state


# Movement
new_X = pos_X=0
new_Y = pos_Y=0
X_vals=[]
Y_vals=[]

current_pos=0,0
new_pos=0,0

no_moves=False

XY_vals=[]

directional_moves=[(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]

for i in range(t_max):    
    steady_time = simulate_growth(N0, M, k, h)

    # print(i)
    while(True):

        current_pos=pos_X,pos_Y

        new_move = random.choice(directional_moves)

        new_X= pos_X+new_move[0]
        new_Y= pos_Y+new_move[1]

        new_pos = new_X, new_Y

        if new_pos not in XY_vals:
            pos_X = new_X
            pos_Y = new_Y
            current_pos = new_pos
            break    

        possible_moves=[]
        new_moves=0

        for move in directional_moves:
            move = tuple(move)  
            potential_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            possible_moves.append(potential_pos)
        
        for poss in possible_moves:
            if poss not in XY_vals:
                new_moves+=1
            
        if new_moves==0:
            print(i)
            print("All adjacent cells are occupied. Stopping simulation")
            no_moves=True
            break

    if no_moves:
        break

    X_vals.append(pos_X)
    Y_vals.append(pos_Y)
    XY_vals.append(new_pos)




plt.plot(X_vals, Y_vals, marker='o', markersize=3, color='grey', linestyle='-')
plt.grid(True)
plt.show()
